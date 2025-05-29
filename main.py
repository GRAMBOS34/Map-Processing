"""
What we're going to do here is to create an app that shows what the makeblock 'sees'

Essentially we'll have a graph that shows the coordinates of where the points are
with lines connecting to each of them

we'll have a 6x6m area because i don't have enough time to think of 
having the area increase in size 

However, this will change depending on the size of the detected area
"""

# TODO: Create a GUI where i click on a grid and the coordinates will be stored in an array (2d, 1d, it doesn't matter)

import tkinter as tk

# Lmfao idk how this works i literally just copied it from AI because I was running out of time lol
# You'd be surprised how much code is usually either copied or AI-Generated in these types of things
# However, you'd learn more if you actually did this yourself rather than have someone/something else
# do it for you
class GridWindow:
    def __init__(self, master):
        self.master = master
        master.title("Robot Mapping")

        # ------------ Frame for Grid Space ----------------
        self.gridFrame = tk.Frame(master)
        self.gridFrame.pack(side=tk.LEFT, padx=10, pady=10)
        self.grid_size = 600
        self.canvas = tk.Canvas(self.gridFrame, width=self.grid_size, height=self.grid_size, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.onClick)

        self.coordinates = []
        self.dotRadius = 3

        # ------------ Frame for Buttons ----------------
        self.buttonFrame = tk.Frame(master)
        self.buttonFrame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        # Clear button
        self.clearButton = tk.Button(self.buttonFrame, text="Clear Grid", command=self.clearCanvas)
        self.clearButton.pack(pady=5)

        # Send Coordinates
        self.sendButton = tk.Button(self.buttonFrame, text="Send Coordinates", command=self.sendCoordinates)
        self.sendButton.pack(pady=5)

    def onClick(self, event):
        x = event.x
        y = event.y
        self.coordinates.append((x, y))
        self.drawDot(x, y)
        print(f"Clicked at: ({x}, {y})")
        print(f"Coordinates array: {self.coordinates}")

    def drawDot(self, x, y):
        x1 = x - self.dotRadius
        y1 = y - self.dotRadius
        x2 = x + self.dotRadius
        y2 = y + self.dotRadius
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue")

    def clearCanvas(self):
        self.canvas.delete("all")  # Delete all items on the canvas
        self.coordinates = []
        print("Canvas cleared. Coordinates array reset.")

    def sendCoordinates(self):
        print(f"Current coordinates: {self.coordinates}")

root = tk.Tk()
grid_window = GridWindow(root)
root.mainloop()