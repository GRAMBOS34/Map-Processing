import event, time, cyberpi, mbot2
import network
import urequests

# -------- WIFI CONFIG --------
# Change if needed
WIFI_SSID = "Jumawan Wifi"
WIFI_PASSWORD = "wifi.1234"

@event.start
def on_start():
    # Connects to the internet on startup (ssid, password)
    cyberpi.wifi.connect(WIFI_SSID, WIFI_PASSWORD)
    cyberpi.display.show_label("Connected to Wifi", 12, "center", index= 0)

# --------------------- Manual Control ---------------------
# Sends messages through wifi to the CyberPi on the bot
@event.is_press('left')
def cmd_forward():
    cyberpi.wifi_broadcast.set("Forward", "Forward")
    
@event.is_press('right')
def cmd_back():
    cyberpi.wifi_broadcast.set("Back", "Back")
    
@event.is_press('up')
def cmd_right():
    cyberpi.wifi_broadcast.set("Turn Right", "Right")
    
@event.is_press('down')
def cmd_left():
    cyberpi.wifi_broadcast.set("Turn Left", "Left")
    
@event.is_press('middle')
def cmd_stop():
    cyberpi.wifi_broadcast.set("Stop", "Stop")
    
# -------- WEB SERVER DETAILS --------
# Change the url after launching your web server
BASE_URL = "http://192.168.0.160:8080"
TELEMETRY_SERVER_URL = BASE_URL + "/telemetry"
INSTRUCTION_SERVER_URL = BASE_URL + "/instruct"

# Sends a POST request to the webserver
def send_post_request(url, data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = urequests.post(url, json=data, headers=headers)
        cyberpi.display.show_label("POST request sent.", 12, "center", index= 0)
        cyberpi.display.show_label(response.status_code, 12, "center", index= 0)
        try:
            cyberpi.display.show_label(response.json(), 12, "center", index= 0)
        except ValueError:
            cyberpi.display.show_label(response.text, 12, "center", index= 0)
        finally:
            response.close()
    except OSError as e:
        cyberpi.display.show_label(e)
    
# Gets the data from the server
def get_new_instrcutions(url):
    try:
        response = urequests.get(url)
        cyberpi.display.show_label("GET request sent.")
        cyberpi.display.show_label(response.status_code)

        if response.status_code == 200: # HTTP 200 OK
            data = response.json()
            response.close()
            return data
        else:
            cyberpi.display.show_label(response.text)
            response.close()
            return None
    except OSError as e:
        cyberpi.display.show_label(e)
        return None

# Sends the telemetry to the web server
@cyberpi.event.mesh_broadcast("Telemetry")
def show_distance():
    data = cyberpi.wifi_broadcast.get("Telemetry")
    send_post_request(TELEMETRY_SERVER_URL, {"Telemetry": data})

# -------- NO LINE FOLLOW --------
@event.is_press('a')
def start_no_line_follow():
    # this function just starts the no line follow
    # the rest is just recursion ig 
    # this is so that we only need to make calls when we need to  
    next_move = get_new_instrcutions(INSTRUCTION_SERVER_URL)
    cyberpi.display.show_label(next_move["instruction"], 12, 'center', index=0)
    cyberpi.wifi_broadcast.set("next_move", next_move)
    
@cyberpi.event.mesh_broadcast("move_complete")
def no_line_follow():
    # it doesn't need to verify anymore since if this signal is sent
    # it guarantees that it's done
    next_move = get_new_instrcutions(INSTRUCTION_SERVER_URL)
    cyberpi.display.show_label(next_move["instruction"], 12, 'center', index=0)
    cyberpi.wifi_broadcast.set("next_move", next_move)
    
@cyberpi.event.mesh_broadcast('path_complete')
def path_complete():
    cyberpi.display.show_label("Path Fully Traversed", 12, 'center', index=0)
    