import math

# Gets the distance between two points
def getDistance (coords1, coords2) -> float:
    
    # Calculate the distance
    xDistComponent = abs(coords2[0] - coords1[0]) # Get the absolute value since we only need distance and not direction
    yDistComponent = abs(coords2[1] - coords1[1]) # Same here

    distance = math.sqrt((xDistComponent**2) + (yDistComponent**2)) # Pythagorean theorem

    return distance

# Gets the next turning angle
# the math will be explained within the function
# coords will be taken as a tuple of two integers
def getTurnAngle(previousPointCoords, currentPointCoords, nextPointCoords) -> float:
    
    # Get distances between coordinates
    distA = getDistance(previousPointCoords, currentPointCoords)
    distB = getDistance(currentPointCoords, nextPointCoords)
    distC = getDistance(previousPointCoords, nextPointCoords)

    """
    This formula just rearranges the Law of Cosines to get the angle
    That's why there's an arccos in the formula
    For a deeper explanation, check the file labeled (LocationTracking_getTurnAngle)
    """
    turnAngle = math.acos(((distA**2) + (distB**2) - (distC**2))/(2 * distA * distC))

    return turnAngle