import event, time, cyberpi, mbot2

@event.is_press('a')
def serial_msg_test_mode():
    # Serial message send test
    cyberpi.upload_broadcast.set("Serial Message Test Send from Handheld CyberPi", 0)

@event.start
def on_start():
    # Connects to the internet on startup (ssid, password)
    cyberpi.wifi.connect("Jumawan Wifi", "wifi.1234")
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

@cyberpi.event.mesh_broadcast("Telemetry")
def show_distance():
    data = cyberpi.wifi_broadcast.get("Telemetry")
    cyberpi.upload_broadcast.set("Telemetry", data)