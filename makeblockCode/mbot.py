import event, time, cyberpi, mbot2, mbuild, random

# -------- WIFI CONFIG --------
# Change if needed
WIFI_SSID = "ssid"
WIFI_PASSWORD = "password"

@event.start
def on_start():
    # Connects to the internet on startup (ssid, password)
    cyberpi.wifi.connect(WIFI_SSID, WIFI_PASSWORD)
    cyberpi.display.show_label("Connected to Wifi", 12, "center", index= 0)

# --------------------- Controls ---------------------
rotation_speed = 60
turn_speed = 30

# --- For telemetry ---
WHEEL_CIRCUMFERENCE = 202.38 # in millimetres (mm)
travel_speed = rotation_speed * (WHEEL_CIRCUMFERENCE / 60) # mm/s
distance_travelled = 0
time_elapsed = 0
last_call_time = None

def send_data():
    # Get the coterminal yaw angle within [0, 360)
    # This angle is important so our calculations can be easier
    coterminal_angle = cyberpi.get_rotation('z')

    if coterminal_angle > 0:
        while not (0 <= coterminal_angle <= 360):
            coterminal_angle -= 360

    if coterminal_angle < 0:
        while not (0 <= coterminal_angle <= 360):
            coterminal_angle += 360
    
    data = [distance_travelled, coterminal_angle]
    cyberpi.wifi_broadcast.set("Telemetry", data)
    cyberpi.display.show_label(coterminal_angle, 12, "center", index= 0)

def dist_timer():
    global distance_travelled, last_call_time
    
    current_time = cyberpi.timer.get()  # Get current time in milliseconds
    
    if last_call_time is not None:
        time_elapsed_ms = current_time - last_call_time
        time_elapsed_sec = time_elapsed_ms / 1000  # Convert to seconds
        distance_travelled = (travel_speed * time_elapsed_sec) * 100 # distance in cm

    send_data()
    
    last_call_time = current_time  # Update timestamp

@cyberpi.event.mesh_broadcast("Forward")
def forward():
    dist_timer()
    mbot2.forward(rotation_speed)

@cyberpi.event.mesh_broadcast("Back")
def back():
    dist_timer()
    mbot2.backward(rotation_speed)
    
@cyberpi.event.mesh_broadcast("Turn Right")
def right():
    send_data()
    mbot2.turn_right(rotation_speed)
    
@cyberpi.event.mesh_broadcast("Turn Left")
def left():
    send_data()
    mbot2.turn_left(rotation_speed)
    
@cyberpi.event.mesh_broadcast("Stop")
def stop():
    send_data()
    mbot2.EM_stop("ALL")
    
# --------------------- No Line Follow ---------------------
# Traverse to a new point set by the instruction from the raspberry pi
@cyberpi.event.mesh_broadcast("next_move")
def next_point_traverse():
    data = cyberpi.wifi_broadcast.get("next_move")["instruction"]
    
    if data[2] == True:
        cyberpi.wifi_broadcast.set("path_complete")
        
    else: 
        # Get coterminal angle
        coterminal_angle = cyberpi.get_rotation('z')

        if coterminal_angle > 0:
            while not (0 <= coterminal_angle <= 360):
                coterminal_angle -= 360

        if coterminal_angle < 0:
            while not (0 <= coterminal_angle <= 360):
                coterminal_angle += 360
        
        angle_deviation = coterminal_angle - data[1] # get angle deviation
        mbot2.turn(angle_deviation) # adjust accordingly
        
        # Move forward
        mbot2.straight(data[0])
        cyberpi.wifi_broadcast.set("move_complete")
        
# --------------------- Free Roam ---------------------
# This mode doesn't do anything special, it just uses the ultrasonic sensor
# to avoid obstacles without any complex logic, it's all just random
@event.is_press('a')
def free_roam():
    
    while True:
        if(mbuild.ultrasonic2.get(1) >= 300):
            # if we can see that there's nothing in front of us, move forward
            # 300 here is 3m by the way
            mbot2.forward(rotation_speed)
            
        else:
            if(mbuild.ultrasonic2.get(1) < 20):
                direction = random.randint(1, 3) # picks a random number
                
                # turns are like that because it compensates a little because
                # it has an error of 4 degrees +- 1.2 degrees
                # if you want to know how I know this, I wrote a script
                # to turn it around while showing the current angle
                # and ran it around 10 times and found the average and the standard deviation
                # ave: 175.5 deg and standard dev of 1.28 deg
                # although if you mess around with this yourself you might find other values so 
                # try finding it out for yourself too
                
                if direction == 1:
                    mbot2.turn(94)
                    
                if direction == 2:
                    mbot2.turn(-94)
                    
                if direction == 3:
                    mbot2.turn(184)
                
            else:
                mbot2.forward(rotation_speed)


# --------------------- Line Following ---------------------
@event.is_press('b')
def lineFollow():
    travelSpeed = 30
    while True:
        cyberpi.display.show_label(mbuild.quad_rgb_sensor.get_offset_track(1), 12, "center", index= 0)
        
        # Basically, if the middle two sensors detects a line,
        # it will continue following it, however, if only one of them sees it
        # it will turn to make sure both sensors can see a line
        
        if mbuild.quad_rgb_sensor.is_line("any", 1):
            if mbuild.quad_rgb_sensor.get_line_sta("middle", 1) == 3:
                mbot2.forward(travelSpeed)
                
            if mbuild.quad_rgb_sensor.get_line_sta("middle", 1) == 2:
                mbot2.turn_left(travelSpeed)
                
            if mbuild.quad_rgb_sensor.get_line_sta("middle", 1) == 1:
                mbot2.turn_right(travelSpeed)
                
        else:
            mbot2.forward(-travelSpeed) # move backward