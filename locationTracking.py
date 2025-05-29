import math

class locationTrack:

    # Doesn't really do much rn as this is where we're supposed to initialize values
    def __init__(self):
        pass
    
    # Gets the distance between two points
    def getDistance (self, coords1:tuple, coords2:tuple) -> float:
        
        # Checks if the given coordinates are only within two dimensions
        # Just in case
        if len(coords1) != 2 or len(coords2) != 2:
            # this line pretty much stops the program because it throws an error
            raise Exception("Coordinates don't exist, try adding or removing a value because this function only works with two dimensions")
        
        # Calculate the distance
        xDistComponent = abs(coords2[0] - coords1[0]) # Get the absolute value since we only need distance and not direction
        yDistComponent = abs(coords2[1] - coords1[1]) # Same here

        distance = math.sqrt((xDistComponent**2) + (yDistComponent**2)) # Pythagorean theorem

        return distance

    # Gets the next turning angle
    # the math will be explained within the function
    # coords will be taken as a tuple of two integers
    def getTurnAngle(self, previousPointCoords:tuple, currentPointCoords:tuple, nextPointCoords:tuple) -> float:

        # Checks if the given coordinates are only within two dimensions
        # Just in case
        if len(previousPointCoords) != 2 or len(currentPointCoords) != 2 or len(nextPointCoords) != 2:
            # this line pretty much stops the program because it throws an error
            raise Exception("Coordinates don't exist, try adding or removing a value because this function only works with two dimensions")
        
        # Get distances between coordinates
        distA = locationTrack.getDistance(self, previousPointCoords, currentPointCoords)
        distB = locationTrack.getDistance(self, currentPointCoords, nextPointCoords)
        distC = locationTrack.getDistance(self, previousPointCoords, nextPointCoords)

        """
        This formula just rearranges the Law of Cosines to get the angle
        That's why there's an arccos in the formula
        For a deeper explanation, check the file labeled (LocationTracking_getTurnAngle)
        """
        turnAngle = math.acos(((distA**2) + (distB**2) - (distC**2))/(2 * distA * distC))

        return turnAngle