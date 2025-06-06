# Robot Map Processing

I really just don't have a better name for this.

But this is the code to the robot shown during the club selling

If the code seems unreadable at certain parts I'm sorry I really tried lol
but it's kinda hard to explain what I'm doing when the code itself is somewhat spaghetti

## How to install (Currently pending)

1. **Install python3 and pip** (find a tutorial for that its pretty easy) OR use an IDE like **Pycharm** or smth

   - Make sure that you add it to PATH if you install on Windows

2. _(Skip this if you used an IDE)_ **Install a code editor**

   - I personally use VS Code but use anything you want

3. Open a terminal in the directory you installed this project and run this command:

   `pip install -r requirements.txt`

4. Connect it up to the hardware, here's a list

   - Raspberry Pi 4 Model b
   - Makeblock mBot neo
   - Your computer

5. Put code in the Makblock mBot neo

   - If you are on Windows: install the ide on their [website](mblock.cc) and code there

   - If you are on Linux (like me):
     - Go to their [website](mblock.cc)
     - Install the mLink2
     - Run this command in the terminal
       ```bash
       sudo mblock-mlink start
       ```
     - Code as normal
     - Go to their website and add their code there
     - Upload to the makeblock devices

## How to use

1. Run the webserver on the Raspberry Pi

   - Optional: If you have a screen, run the main.py there too

2. Turn on both makeblock devices

3. Do either one of these:
   - Move the joystick on the handheld cyberpi for **Manual Control**
   - Press the square button on the mbot for **Free Roam**
   - Press the triangle button on the mbot for **Line Following**
   - Press the triangle button on the handheld cyberpi after uploading a path on the Raspberry Pi webserver for **No Line Follow**

## Notes i.e. _(Things idk how to fix so that's a feature now)_

1. Currently, the grid shown on the main.py isn't aligned to what you might expect from the robot, so make sure that the mbot is on the bottom left of the area you're letting it use facing right. Just imagine it on the cartesian plane with the heading 0 degrees/radians and orient it that way
