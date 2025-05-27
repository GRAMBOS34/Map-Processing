"""
What we're going to do here is to create an app that shows what the makeblock 'sees'

Essentially we'll have a graph that shows the coordinates of where the points are
with lines connecting to each of them

we'll have a 300cm by 300cm area because i don't have enough time to think of 
having the area increase in size 
"""

import matplotlib.pyplot as plt
import numpy as np

x_coords = [1, 2, 3, 4, 5]
y_coords = [2, 4, 1, 3, 5]

plt.plot(x_coords, y_coords, marker='o', linestyle='none')

plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Title of the plot")
plt.grid(True)

plt.show()