import string

# This method will calculate all the rotations for a given term
def calculateRotations(term):
    rotations = []
    # Check if term is not empty
    if term:
        rotation = term + '$'
        rotations.append(rotation)
        for char in term:
            # Each iteration place the first char at the end of rotation
            rotation = rotation[1:] + char
            rotations.append(rotation)
    return rotations

# This method will create a permuterm index based on the given dictionary
def createPermutermIndex(dictionary):
    permuIndex = {}
    for term in dictionary:
        # Calculate all the rotations for a term
        rotations = calculateRotations(term)
        # Add each rotation to the index with the corresponding term
        for rotation in rotations:
            permuIndex[rotation] = term
    return permuIndex

