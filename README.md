# Robot Demonstration Thing

I really just don't have a better name for this.

But this is the code to the robot shown during the club selling

If the code seems unreadable at certain parts I'm sorry I really tried lol
but it's kinda hard to explain what I'm doing when the code consists of 1/4 written by AI, 2/4 copy-paste, 1/4 hubris

Have fun, hopefully you can bear reading the code because I **_know_** you'll also say the same things about your own code, how it's "unreadable" or "spaghetti" it'll happen trust me

## How to install stuff

1. **Install python3 and pip** (find a tutorial for that its pretty easy) OR use an IDE like **Pycharm** or smth

   - Make sure that you add it to PATH if you install on Windows
   - Also if you use an IDE, the process might change so if you do, you'll be on your own idk how to help you with that sorry

2. _(Skip this if you used an IDE)_ **Install a code editor**

   - I personally use VS Code but use anything you want but if you'll SSH into the Raspberry Pi (more on this later), install something like **_Vim_** on the Raspberry Pi

3. Open a terminal in the directory you installed this project and run this command:

   `pip install -r requirements.txt`

4. Connect it up to the hardware, here's a list

   - Raspberry Pi 4 Model b
   - Makeblock mBot neo
   - Your computer

5. Put code in the Makblock mBot neo

   - If you are on Windows: install the ide on their [website](mblock.cc) and code there

   - If you are on Linux (like me) or don't want to install the ide:
     - Go to their [website](mblock.cc)
     - Install the mLink2
     - Run this command in the terminal (idk what it is on Windows)
       ```bash
       sudo mblock-mlink start
       ```
     - Code as normal
     - Go to their website and add their code there
     - Upload to the makeblock devices

## How to use

1. Connect the Raspberry Pi to power, a monitor, mouse, and keyboard

   - Alternatively: you can just SSH into the Raspberry Pi, here's a tutorial:
     https://www.raspberrypi.com/documentation/computers/remote-access.html#ssh

2. Run the webserver on the Raspberry Pi

   - Optional: If you have a screen, run the main.py there too

3. Check if the url in the handheld CyberPi matches the url shown in the console of the flask server

4. Turn on both makeblock devices

5. Do either one of these:
   - Move the joystick on the handheld cyberpi for **Manual Control**
   - Press the square button on the mbot for **Free Roam**
   - Press the triangle button on the mbot for **Line Following**
   - Press the triangle button on the handheld cyberpi after uploading a path on the Raspberry Pi webserver for **No Line Follow**

## However,

If you want to switch modes, you'll have to turn it off and on again because I got lazy sorry lol

## Notes i.e. _Things idk how to fix so they're features now_

1. Currently, the grid shown on the main.py isn't aligned to what you might expect from the robot, so make sure that the mbot is on the bottom left of the area you're letting it use facing right. Just imagine it on the cartesian plane with the heading 0 degrees/radians and orient it that way.

2. There are a few more things I wish I could've added but didn't do it out of either complexity, oversight, or straight-up laziness. Here are some of those things and hopefully, this could be like an assignment given to the kids:

   - Auto-stop during manual mode (like it stops before it hits a wall)

   - A way to separate each mode (because right now, you can just interrupt any mode using the joystick on the handheld)

     - What I mean by this is that it should have a dedicated switch to change modes and if you are in a specific mode, you can't use the other controls unless you switch the mode

   - In main.py, make the canvas bigger while not changing the coordinates of the points. Since right now, the window where you click to add points for the mbot to traverse is dependent on the coordinates of the pixel, so you should add a feature where if you resize the window, if you click on the window to add a point, it would convert those coordinates to the size of the area you're using. For example, you'll get the same coordinates regardless if the size of the box was 200x200px or 900x900px, it would still be able to convert to the (for example) 200x200cm area

     - also, the items in the window should resize relative to the window size (or just have it fixed if you're lazy)

   - A scout mode:
     - Basically, it will be able to map out its own environment using the ultrasonic sensor
     - I originally intended to do this but then realized it was too complex to do within like a week soooo...
     - The idea is that it will spin around, take the distance from there to that point and the current angle it is at, and use it to plot a point on a plane so that it'll know the bounds of that area
     - The range of the ultrasonic sensor is 3m so in theory you could have a circle with a diametre of 6m as the "scan area"
     - Basically doing [SLAM](https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping) (Simultaneous Localization and Maping)
     - Also this was supposed to be a module I put in the /raspberryPi/dependencies folder but since I scrapped it, only instructionSend.py is there

3. The reason why I didn't do the first two stated in no. 2 was because idk how to block inputs in the makeblock so ¯\_(ツ)\_/¯ and the fourth one was, in theory, not **_that_** complicated, it's just that the more I thought it over, I just couldn't really think of the point of it besides mental masturbation. I'm sure that you can think of a better use for this though. Or, you might even come up with ideas of your own. Like using the colour sensor for **_anything_** other than line-following.
