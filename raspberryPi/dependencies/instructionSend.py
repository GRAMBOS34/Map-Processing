import math
import json
import os

# Creates the next direction
def create_direction(current_coordinate:tuple, next_coordinate:tuple):
    # Converts the cartesian coordinates into polar coordinates
    # That can be easily used to direct the robot

    x_diff = next_coordinate[0] - current_coordinate[0]
    y_diff = next_coordinate[1] - current_coordinate[1]
    
    # Gets the distance
    distance = math.sqrt((x_diff**2) + (y_diff**2))

    # Gets the angle (converts from radians to degrees)
    angle = (math.atan2(y_diff, x_diff) * 180) / 3.14
    
    return distance, angle # distance in cm

# Gets the next point
def next_point(currentIndex:int) -> tuple:   
    MASTER_FOLDER = "Map-Processing" # this is the name of the folder your project is on
    relativeCoordinateFilePath = os.path.join("..", MASTER_FOLDER, "coordinates.json") # gets the relative path
    absoluteCoordinateFilePath = os.path.realpath(relativeCoordinateFilePath) # gets the aboslute path
    
    with open(absoluteCoordinateFilePath, "r") as file: # Opens the coordinates.json file
        data = json.load(file) # loads the file into a usable array/dictionary (depends on the formatting)

        """
        Basically:
        if accessing data[currentIndex + 1] doesn't throw an out-of-range error, calculate 
        the polar coordinates and return it
        
        otherwise, consider it as the end of the path and just return is_end as True
        """
        try:
            current_coordinate = data[currentIndex]
            next_coordinate = data[currentIndex + 1]

            print(current_coordinate)

            new_point = create_direction(current_coordinate, next_coordinate)

            # [distance, angle, is_end]
            return [new_point[0], new_point[1], False]

        except:
            # [distance, angle, is_end]
            new_point = [0, 0, True]

            return new_point