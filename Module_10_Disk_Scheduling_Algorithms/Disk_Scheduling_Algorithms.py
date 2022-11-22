import numpy as np
from array import array
import random

def randomGen(qty: int) -> array:
    randomNumbs = np.random.randint(0,10,size=qty)
    print(randomNumbs)
    return randomNumbs

def fairnessTest(initArray: array, testArray: array) -> tuple:
    i = 0
    traversedTracksScan = 0
    while i < testArray.size / 2 - 1:
        currentTrack = testArray[1, i]
        nextTrack = testArray[1, i+1]

        traversedTracksScan = traversedTracksScan + abs(nextTrack - currentTrack)

        i += 1

    fairnessScore = 0
    i = 0
    while i < initArray.size / 2 - 1:
        fairnessScore = fairnessScore + testArray[0,i] - initArray[0,i]
        i += 1

    return traversedTracksScan, fairnessScore

def fifoTest(fifoTestArray: array) -> int:
    i = 0
    traversedTracksFifo = 0

    while i < fifoTestArray.size - 1:
        currentTrack = fifoTestArray[i]
        nextTrack = fifoTestArray[i + 1]
        traversedTracksFifo = traversedTracksFifo + abs(nextTrack - currentTrack)
        i += 1

    return traversedTracksFifo

def scanTest(fifoArray: array) -> int:
    i = 0
    j = 1

    # Create a copy of the original array for fairness assessment
    idx = np.arange(0, fifoArray.size, 1)
    fifoArray = np.vstack((idx, fifoArray))
    fifoCopy = np.copy(fifoArray)

    # Create a Scan scheduled array from original FIFO Array
    scanTestArray = np.zeros((2,10), dtype=int)

    scanTestArray[ : ,0] = fifoArray[ : ,0]
    fifoArray = np.delete(fifoArray, 0, 1)

    i = 0
    j = 0
    while j < fifoArray.size / 2:
        currentTrack = scanTestArray[ : ,i]
        nextTrack = fifoArray[ : ,j]

        if nextTrack[1] >= currentTrack[1]:
            scanTestArray[0,i+1] = nextTrack[0]
            scanTestArray[1,i+1] = nextTrack[1]
            fifoArray = np.delete(fifoArray, j, 1)
            i += 1
        else:
            j += 1
    fifoArray = fifoArray[:, fifoArray[1, :].argsort()[::-1]]

    # Add remaining values to the new Scan array in correct order
    j = 0
    while j < fifoArray.size / 2:
        scanTestArray[0,i+1] = fifoArray[0,j]
        scanTestArray[1,i+1] = fifoArray[1,j]
        j += 1
        i += 1

    return fairnessTest(fifoCopy, scanTestArray)

def cScanTest (fifoArray: array) -> int:
    i = 0
    j = 1

    # Create a copy of the original array for fairness assessment
    idx = np.arange(0, fifoArray.size, 1)
    fifoArray = np.vstack((idx, fifoArray))
    fifoCopy = np.copy(fifoArray)

    # Create a Scan scheduled array from original FIFO Array
    cScanTestArray = np.zeros((2,10), dtype=int)

    cScanTestArray[ : ,0] = fifoArray[ : ,0]
    fifoArray = np.delete(fifoArray, 0, 1)

    i = 0
    j = 0
    while j < fifoArray.size / 2:
        currentTrack = cScanTestArray[ : ,i]
        nextTrack = fifoArray[ : ,j]

        if nextTrack[1] >= currentTrack[1]:
            cScanTestArray[0,i+1] = nextTrack[0]
            cScanTestArray[1,i+1] = nextTrack[1]
            fifoArray = np.delete(fifoArray, j, 1)
            i += 1
        else:
            j += 1
    fifoArray = fifoArray[:, fifoArray[1, :].argsort()]

    # Add remaining values to the new Scan array in correct order
    j = 0
    while j < fifoArray.size / 2:
        cScanTestArray[0,i+1] = fifoArray[0,j]
        cScanTestArray[1,i+1] = fifoArray[1,j]
        j += 1
        i += 1

    return fairnessTest(fifoCopy, cScanTestArray)

testArray = randomGen(10)

print(fifoTest(testArray))

# sstfTest

print(scanTest(testArray))

print(cScanTest(testArray))