import numpy as np
from array import array
import random

def randomGen(qty: int) -> array:
    randomNumbs = np.random.randint(0,10,size=qty)
    # indexArray = np.arange(0, qty, 1)
    # print(indexArray)
    # print(randomNumbs)
    # randomNumbs = np.vstack((indexArray, randomNumbs))

    # print(randomNumbs[1][0]) #debug test
    return randomNumbs

def fifoTest(testNumbs: array) -> int:
    i = 0
    traversedTracksFifo = 0

    while i < testNumbs.size - 1:
        currentTrack = testNumbs[i]
        nextTrack = testNumbs[i + 1]
        traversedTracksFifo = traversedTracksFifo + abs(nextTrack - currentTrack)
        i += 1

    return traversedTracksFifo

def scanTest(testNumbs: array) -> int:
    i = 0
    j = 1
    traversedTracksScan = 0

    # Create a copy of the original array for fairness assessment
    fifoArray = np.copy(testNumbs)

    # Put first number in array into list
    scanTracksList = []
    scanTracksList.append(testNumbs[i])

    # For every subsequent number higher than or equal to current, add it to the list
    while j < testNumbs.size - 1:
        currentTrack = testNumbs[i]
        nextTrack = testNumbs[j]
    
        if nextTrack >= currentTrack:
            scanTracksList.append(nextTrack)
            testNumbs = np.delete(testNumbs, i)
            i = j - 1
        else:
            j += 1

    testNumbs = np.delete(testNumbs, i)

    # Sort remaining values in reverse order for Scan method
    testNumbs.sort()
    testNumbs = testNumbs[::-1]

    i = 0    
    # Append remaining items to the list
    while i < testNumbs.size:
        scanTracksList.append(testNumbs[i])
        i += 1 
    
    # Refresh the original array with the new list in Scan order
    testNumbs = np.array(scanTracksList)
    
    i = 0
    fairnessTest = 0
    while i < testNumbs.size - 1:
        currentTrack = testNumbs[i]
        nextTrack = testNumbs[i+1]

        traversedTracksScan = traversedTracksScan + abs(nextTrack - currentTrack)

        i += 1

    i = 0
    j = 0
    fairness = 0

    # Can't figure out a good way to measure fairness with respect to repeats
    while i < fifoArray.size:
        while j < testNumbs.size:
            if fifoArray[i] == testNumbs[j]:
                fairness = fairness + j - i
                break
            j += 1
        i += 1
        j = 0

    print(fairness)
    return traversedTracksScan


testArray = randomGen(10)

# randomGen(100)

print(fifoTest(testArray))

# sstfTest

print(scanTest(testArray))

# cScanTest