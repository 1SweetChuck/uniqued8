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

indexOfOne = digits.index(1)
neighborsOfOne = getNeighborsOfOne(digits, indexOfOne)
neighborsOfOne.sort()
smallestNeighborOfOne = neighborsOfOne[0]

# print(digits)
# print(indexOfOne)
newIndexOfOne = indexOfOne
newDigitsOrder = digits
while newIndexOfOne > 3:
    newDigitsOrder = rotateOnTheta(newDigitsOrder)
    newIndexOfOne = newDigitsOrder.index(1)
    # print(newDigitsOrder)
    # print(newIndexOfOne)

while newIndexOfOne != 0:
    newDigitsOrder = rotateOnOmega(newDigitsOrder)
    newIndexOfOne = newDigitsOrder.index(1)
    # print(newDigitsOrder)
    # print(newIndexOfOne)

indexOfSmallestNeighbor = newDigitsOrder.index(smallestNeighborOfOne)
# print("Index Of Smallest Neighbor: ", indexOfSmallestNeighbor)

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

elif indexOfSmallestNeighbor == 6:
    newDigitsOrder = rotateOnOmega(newDigitsOrder)
    newDigitsOrder = rotateOnTheta(newDigitsOrder)
    newIndexOfOne = newDigitsOrder.index(1)
    indexOfSmallestNeighbor = newDigitsOrder.index(smallestNeighborOfOne)
    # print("Index Of Smallest Neighbor: ", indexOfSmallestNeighbor)

finalString = ""
for intValue in newDigitsOrder:
    finalString += str(intValue)

print(finalString)
