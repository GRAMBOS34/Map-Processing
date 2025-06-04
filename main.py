"""
What we're going to do here is to create an app that shows what the makeblock 'sees'

Essentially we'll have a graph that shows the coordinates of where the points are
with lines connecting to each of them

we'll have a 2x2m area because i don't have enough time to think of 
having the area increase in size 

also using the fulll 6x6m area is just purely gratuitous in it of itself

However, this will change depending on the size of the detected area
"""

import tkinter as tk
import requests
import json

class GridWindow:
    def __init__(self, master):
        self.master = master
        master.title("Robot Mapping")

        """
        Frames are like divs in html
        They're just boxes where we can isolate certain parts of our ui

        In here, I split the grid space and the space for buttons
        so that I don't have to make everything relative to other elements, 
        I can just make boxes that are relative to each other
        (You'll understand how much easier this is if you actually do it)
        """

        # ------------ Frame for Grid Space ----------------
        self.gridFrame = tk.Frame(master)
        self.gridFrame.pack(side=tk.LEFT, padx=10, pady=10)

        # Canvas for the space where you can click
        self.grid_size = 200 # side length in cm
        self.canvas = tk.Canvas(self.gridFrame, width=self.grid_size, height=self.grid_size, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.onClick)
        self.canvas.bind("<Configure>", self.create_grid)

        self.coordinates = [[0,0]]
        self.dotRadius = 5
        self.drawDot(0, 0)

        # ------------ Frame for Buttons ----------------
        self.buttonFrame = tk.Frame(master)
        self.buttonFrame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        # Label
        self.statusLabel = tk.Label(self.buttonFrame, text="None")
        self.statusLabel.pack(pady=5)

        # Clear button
        self.clearButton = tk.Button(self.buttonFrame, text="Clear Grid", command=self.clearCanvas)
        self.clearButton.pack(pady=5)

        # Send Coordinates
        self.sendButton = tk.Button(self.buttonFrame, text="Send Coordinates", command=self.sendCoordinates)
        self.sendButton.pack(pady=5)

    def create_grid(self, event=None):
        w = self.canvas.winfo_width() # Get current width of canvas
        h = self.canvas.winfo_height() # Get current height of canvas
        self.canvas.delete('grid_line') # Will only remove the grid_line

        # Creates all vertical lines at intevals of 50 cm
        for i in range(0, w, 50):
            self.canvas.create_line([(i, 0), (i, h)], tag='grid_line')

        # Creates all horizontal lines at intevals of 50 cm
        for i in range(0, h, 50):
            self.canvas.create_line([(0, i), (w, i)], tag='grid_line')

    def onClick(self, event):
        # Adds the coordinate to the array
        x = event.x
        y = event.y

        if len(self.coordinates) != 0:
            prevCoords = self.coordinates[len(self.coordinates)-1] 
            self.drawLine(prevCoords[0], prevCoords[1], x, y)

        self.coordinates.append((x, y)) # add coordinates to the coordinates array
        self.drawDot(x, y)
        self.statusLabel.config(text=f"Clicked at: ({x}, {y})") # Changes the status text

    def drawDot(self, x, y):
        # Determines dimensions of the dot
        x1 = x - self.dotRadius
        y1 = y - self.dotRadius
        x2 = x + self.dotRadius
        y2 = y + self.dotRadius
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue", tag='path') # Draws the dot

    def drawLine(self, prevX, prevY, newX, newY):
        # Draws a line between two points
        self.canvas.create_line(prevX, prevY, newX, newY, fill="black", width=3, arrow="last", tag='path')

    def clearCanvas(self):
        # Clears the grid space and removes all the coordinates
        self.canvas.delete("path")  # Deletes only items with the tag "path"
        self.coordinates = [] # Resets the coordinates array
        self.statusLabel.config(text="Canvas cleared. Coordinates array reset.")

    def sendCoordinates(self):
        #? Adds the coordinates to a txt file which will be read by the map reader (idk what to call it for now)

        # TODO: make a function to send the data to the Raspberry Pi

        # Server URL
        #! CHANGE THE URL IF NEEDED 
        url = 'http://192.168.0.141:8080/new_coords'

        # Send the array as JSON
        response = requests.post(url, json={'coordinates': self.coordinates})

        # Print the response
        print(response.json())

        # Clears the grid space and removes all the coordinates
        # self.canvas.delete("path")  # Delete only items with the tag "path"
        self.coordinates = [] # Resets the coordinates array
        self.statusLabel.config(text="Coordinates Sent")

# Shows the window
root = tk.Tk()
grid_window = GridWindow(root)
root.mainloop()