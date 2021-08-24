#!/usr/bin/python

import sys
import re

def badArgExit():
    print("Please run with an 8 digit number with digits 1-8 and no repeating digits. Example 12345678.")
    exit(128)


def getNeighborsOfOne(digits, indexOfOne):
    if indexOfOne == 0:
        return [digits[1], digits[3], digits[6]]
    elif indexOfOne == 1:
        return [digits[0], digits[2], digits[7]]
    elif indexOfOne == 2:
        return [digits[1], digits[3], digits[4]]
    elif indexOfOne == 3:
        return [digits[0], digits[2], digits[5]]
    elif indexOfOne == 4:
        return [digits[2], digits[5], digits[7]]
    elif indexOfOne == 5:
        return [digits[3], digits[4], digits[6]]
    elif indexOfOne == 6:
        return [digits[0], digits[5], digits[7]]
    elif indexOfOne == 7:
        return [digits[1], digits[4], digits[6]]


def rotateOnOmega(startingDigits):
    endingDigits = [startingDigits[3], startingDigits[0], startingDigits[1], startingDigits[2],
                    startingDigits[7], startingDigits[4], startingDigits[5], startingDigits[6]]
    return endingDigits


def rotateOnTheta(startingDigits):
    endingDigits = [startingDigits[1], startingDigits[7], startingDigits[4], startingDigits[2],
                    startingDigits[5], startingDigits[3], startingDigits[0], startingDigits[6]]
    return endingDigits


def rotateOnPhi(startingDigits):
    endingDigits = [startingDigits[3], startingDigits[2], startingDigits[4], startingDigits[5],
                    startingDigits[7], startingDigits[6], startingDigits[0], startingDigits[1]]
    return endingDigits

##################
# Validate Input #
##################

if len(sys.argv) != 2:
    badArgExit()

userInput = str(sys.argv[1])
if len(userInput) != 8:
    badArgExit()

pattern = re.compile('\d{8}')
match = pattern.match(userInput)

if match is None:
    badArgExit()

if match.start() != 0 or match.end() != 8:
    badArgExit()

digits = [int(char) for char in userInput]

if not all(elem in digits for elem in [1,2,3,4,5,6,7,8]):
    badArgExit()

##################################
# Calculate Lowest Configuration #
##################################

# Find what position the 1 is in
indexOfOne = digits.index(1)

# Determine the values of the three faces adjacent to the 1
neighborsOfOne = getNeighborsOfOne(digits, indexOfOne)

# Determine which of the three adjacent faces has the smallest value
neighborsOfOne.sort()
smallestNeighborOfOne = neighborsOfOne[0]

# print(digits)
# print(indexOfOne)
newIndexOfOne = indexOfOne
newDigitsOrder = digits

# If the 1 is on the bottom of the d8, rotate to the top.
# In other words if the 1 is in the last four digits of the input
# 'rotate' the d8 to put the one in the first for digits of the input
while newIndexOfOne > 3:
    newDigitsOrder = rotateOnTheta(newDigitsOrder)
    newIndexOfOne = newDigitsOrder.index(1)
    # print(newDigitsOrder)
    # print(newIndexOfOne)

# Now that the 1 is on the visible side of the d8, rotate the
# dice to put it in the upper right quadrant.
# IOW, now that the 1 is in the first four digits 'rotate' the d8 so
# that the 1 is moved to the first digit
while newIndexOfOne != 0:
    newDigitsOrder = rotateOnOmega(newDigitsOrder)
    newIndexOfOne = newDigitsOrder.index(1)
    # print(newDigitsOrder)
    # print(newIndexOfOne)

# Figure out where the least valued adjacent face is in relation to the 1
indexOfSmallestNeighbor = newDigitsOrder.index(smallestNeighborOfOne)
# print("Index Of Smallest Neighbor: ", indexOfSmallestNeighbor)

# if the smallest neighbor is in the upper left quadrant rotate the d8
# to keep the 1 in place and put the smallest neighbor in the lower right
if indexOfSmallestNeighbor == 3:
    newDigitsOrder = rotateOnTheta(newDigitsOrder)
    newDigitsOrder = rotateOnTheta(newDigitsOrder)
    newDigitsOrder = rotateOnTheta(newDigitsOrder)
    newDigitsOrder = rotateOnOmega(newDigitsOrder)
    newDigitsOrder = rotateOnOmega(newDigitsOrder)
    newDigitsOrder = rotateOnOmega(newDigitsOrder)
    newIndexOfOne = newDigitsOrder.index(1)
    indexOfSmallestNeighbor = newDigitsOrder.index(smallestNeighborOfOne)
    # print("Index Of Smallest Neighbor: ", indexOfSmallestNeighbor)

# else if the smallest neighbor is on the far side of the d8, under the 1,
# rotate the d8 keep the 1 in place and put the smallest neighbor in the lower right
elif indexOfSmallestNeighbor == 6:
    newDigitsOrder = rotateOnOmega(newDigitsOrder)
    newDigitsOrder = rotateOnTheta(newDigitsOrder)
    newIndexOfOne = newDigitsOrder.index(1)
    indexOfSmallestNeighbor = newDigitsOrder.index(smallestNeighborOfOne)
    # print("Index Of Smallest Neighbor: ", indexOfSmallestNeighbor)

# convert the rotated digits order to a string and print it.
finalString = ""
for intValue in newDigitsOrder:
    finalString += str(intValue)

print(finalString)
