import numpy as np
from array import array
import random

def randomGen(qty: int) -> array:
    randomNumbs = np.random.randint(0,10,size=qty)
    print(randomNumbs)
    return randomNumbs

def fairnessTest(initArray: array, testArray: array) -> int:
    indexArray = np.arange(0, testArray.size, 1)
    testArray = np.vstack((indexArray, testArray))


def fifoTest(fifoTestArray: array) -> int:
    i = 0
    traversedTracksFifo = 0

    while i < fifoTestArray.size - 1:
        currentTrack = fifoTestArray[i]
        nextTrack = fifoTestArray[i + 1]
        traversedTracksFifo = traversedTracksFifo + abs(nextTrack - currentTrack)
        i += 1

    return traversedTracksFifo

def scanTest(scanTestArray: array) -> int:
    i = 0
    j = 1
    traversedTracksScan = 0

    # Create a copy of the original array for fairness assessment
    fifoArray = np.copy(scanTestArray)
    # indexArray = np.arange(0, scanTestArray.size, 1)
    # fifoArray = np.vstack((indexArray, testArray))

    # Put first number in array into list
    scanTracksList = []
    scanTracksList.append(scanTestArray[i])

    # For every subsequent number higher than or equal to current, add it to the list
    while j < scanTestArray.size - 1:
        currentTrack = scanTestArray[i]
        nextTrack = scanTestArray[j]
    
        if nextTrack >= currentTrack:
            scanTracksList.append(nextTrack)
            scanTestArray = np.delete(scanTestArray, i)
            i = j - 1
        else:
            j += 1

    scanTestArray = np.delete(scanTestArray, i)

    # Sort remaining values in reverse order for Scan method
    scanTestArray.sort()
    scanTestArray = scanTestArray[::-1]

    i = 0    
    # Append remaining items to the list
    while i < scanTestArray.size:
        scanTracksList.append(scanTestArray[i])
        i += 1 
    
    # Refresh the original array with the new list in Scan order
    scanTestArray = np.array(scanTracksList)
    
    # fairnessTest(fifoArray, scanTestArray)
    i = 0
    fairnessTest = 0
    while i < scanTestArray.size - 1:
        currentTrack = scanTestArray[i]
        nextTrack = scanTestArray[i+1]

        traversedTracksScan = traversedTracksScan + abs(nextTrack - currentTrack)

        i += 1

    i = 0
    j = 0
    fairness = 0

    # Can't figure out a good way to measure fairness with respect to repeat values
    while i < fifoArray.size:
        while j < scanTestArray.size:
            if fifoArray[i] == scanTestArray[j]:
                fairness = fairness + j - i
                break
            j += 1
        i += 1
        j = 0

    return traversedTracksScan

def cScanTest (cScanTestArray: array) -> int:
    i = 0
    j = 1
    traversedTracksCscan = 0

    # Create a copy of the original array for fairness assessment
    fifoArray = np.copy(cScanTestArray)

    # Put first number in array into list
    cScanTracksList = []
    cScanTracksList.append(cScanTestArray[i])

    # For every subsequent number higher than or equal to current, add it to the list
    while j < cScanTestArray.size - 1:
        currentTrack = cScanTestArray[i]
        nextTrack = cScanTestArray[j]
    
        if nextTrack >= currentTrack:
            cScanTracksList.append(nextTrack)
            cScanTestArray = np.delete(cScanTestArray, i)
            i = j - 1
        else:
            j += 1

    # Delete highest remaining value, already in list
    cScanTestArray = np.delete(cScanTestArray, i)

    # Sort remaining values in reverse order for Scan method
    cScanTestArray.sort()
    # cScanTestArray = cScanTestArray[::-1]

    i = 0    
    # Append remaining items to the list
    while i < cScanTestArray.size:
        cScanTracksList.append(cScanTestArray[i])
        i += 1 
    
    # Refresh the original array with the new list in Scan order
    cScanTestArray = np.array(cScanTracksList)
    
    # fairnessTest(fifoArray, cScanTestArray)
    i = 0
    fairnessTest = 0
    while i < cScanTestArray.size - 1:
        currentTrack = cScanTestArray[i]
        nextTrack = cScanTestArray[i+1]

        traversedTracksCscan = traversedTracksCscan + abs(nextTrack - currentTrack)

        i += 1

    i = 0
    j = 0
    fairness = 0

    # Can't figure out a good way to measure fairness with respect to repeat values
    while i < fifoArray.size:
        while j < cScanTestArray.size:
            if fifoArray[i] == cScanTestArray[j]:
                fairness = fairness + j - i
                break
            j += 1
        i += 1
        j = 0

    return traversedTracksCscan

def newTest(scanTest: array) -> int:
    i = 0
    j = 1
    traversedTracksScan = 0

    # Create a copy of the original array for fairness assessment
    fifoArray = np.copy(scanTest)


### START NEW SECTION WITHOUT LIST VARIABLE ###
    newArray = np.zeros(scanTest.size, dtype=int)

    newArray[0] = scanTest[0]
    scanTest = np.delete(scanTest, 0)

    i = 0
    j = 0
    # while i < scanTest.size:
    while j < scanTest.size:
        currentTrack = newArray[i]
        nextTrack = scanTest[j]

        if nextTrack >= currentTrack:
            newArray[i + 1] = nextTrack
            scanTest = np.delete(scanTest, j)
            i += 1
        else:
            j += 1
        # i += 1
    scanTest.sort()
    scanTest = scanTest[::-1]

    j = 0
    while j < scanTest.size:
        newArray[i + 1] = scanTest[j]
        j += 1
        i += 1

### END NEW SECTION WITHOUT LIST VARIABLE ###

    return traversedTracksScan

testArray = randomGen(10)

print(fifoTest(testArray))

# sstfTest

print(scanTest(testArray))

print(cScanTest(testArray))

print(newTest(testArray))