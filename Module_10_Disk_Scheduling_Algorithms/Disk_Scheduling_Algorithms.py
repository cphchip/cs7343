import numpy as np
from array import array
import random
import matplotlib.pyplot as plt


def randomGen(qty: int) -> array:
    randomNumbs = np.random.randint(0,99,size=qty)
    print(randomNumbs)
    return randomNumbs

def scheduleConversion(fifoArray: array, scheduleType: str) -> array:
    # Create a new scheduled array from original FIFO Array
    newArray = np.zeros((2,fifoArray.size), dtype=int)

    newArray[ : ,0] = fifoArray[ : ,0]
    fifoArray = np.delete(fifoArray, 0, 1)

    i = 0
    j = 0
    while j < fifoArray.size / 2:
        currentTrack = newArray[ : ,i]
        nextTrack = fifoArray[ : ,j]

        if nextTrack[1] >= currentTrack[1]:
            newArray[0,i+1] = nextTrack[0]
            newArray[1,i+1] = nextTrack[1]
            fifoArray = np.delete(fifoArray, j, 1)
            i += 1
        else:
            j += 1
    
    if scheduleType == "scan":
        fifoArray = fifoArray[:, fifoArray[1, :].argsort()[::-1]]
    elif scheduleType == "cscan":
        fifoArray = fifoArray[:, fifoArray[1, :].argsort()]

    # Add remaining values to the new Scan array in correct order
    j = 0
    while j < fifoArray.size / 2:
        newArray[0,i+1] = fifoArray[0,j]
        newArray[1,i+1] = fifoArray[1,j]
        j += 1
        i += 1


    return newArray

def fairnessTest(initArray: array, testArray: array) -> tuple:
    i = 0
    traversedTracksScan = 0
    maxWaitList = []
    while i < testArray.size / 2 - 1:
        currentTrack = testArray[1, i]
        nextTrack = testArray[1, i+1]

        traversedTracksScan = traversedTracksScan + abs(nextTrack - currentTrack)
        maxWaitList.append(nextTrack - currentTrack)
        i += 1

    maxWait = max(maxWaitList)

    fairnessScore = 0
    i = 0
    while i < initArray.size / 2 - 1:
        fairnessScore = fairnessScore + testArray[0,i] - initArray[0,i]
        i += 1

    return traversedTracksScan, fairnessScore

def maxWait(testArray: array) -> int:
    i = 0
    maxWaitList = []
    while i < testArray.size / 2 - 1:
        currentTrack = testArray[1, i]
        nextTrack = testArray[1, i+1]

        maxWaitList.append(nextTrack - currentTrack)
        i += 1

    maxWait = max(maxWaitList)

    return maxWait

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
    # i = 0
    # j = 1

    # Create a copy of the original array for fairness assessment
    idx = np.arange(0, fifoArray.size, 1)
    fifoArray = np.vstack((idx, fifoArray))
    fifoCopy = np.copy(fifoArray)

    # # Create a Scan scheduled array from original FIFO Array
    # scanTestArray = np.zeros((2,fifoArray.size), dtype=int)

    # scanTestArray[ : ,0] = fifoArray[ : ,0]
    # fifoArray = np.delete(fifoArray, 0, 1)

    # i = 0
    # j = 0
    # while j < fifoArray.size / 2:
    #     currentTrack = scanTestArray[ : ,i]
    #     nextTrack = fifoArray[ : ,j]

    #     if nextTrack[1] >= currentTrack[1]:
    #         scanTestArray[0,i+1] = nextTrack[0]
    #         scanTestArray[1,i+1] = nextTrack[1]
    #         fifoArray = np.delete(fifoArray, j, 1)
    #         i += 1
    #     else:
    #         j += 1
    # fifoArray = fifoArray[:, fifoArray[1, :].argsort()[::-1]]

    # # Add remaining values to the new Scan array in correct order
    # j = 0
    # while j < fifoArray.size / 2:
    #     scanTestArray[0,i+1] = fifoArray[0,j]
    #     scanTestArray[1,i+1] = fifoArray[1,j]
    #     j += 1
    #     i += 1

    scanTestArray = scheduleConversion(fifoArray, "scan")
    print("The Scan max wait time is", maxWait(scanTestArray))

    return fairnessTest(fifoCopy, scanTestArray)

def cScanTest (fifoArray: array) -> int:
    # i = 0
    # j = 1

    # Create a copy of the original array for fairness assessment
    idx = np.arange(0, fifoArray.size, 1)
    fifoArray = np.vstack((idx, fifoArray))
    fifoCopy = np.copy(fifoArray)

    # # Create a Scan scheduled array from original FIFO Array
    # cScanTestArray = np.zeros((2,fifoArray.size), dtype=int)

    # cScanTestArray[ : ,0] = fifoArray[ : ,0]
    # fifoArray = np.delete(fifoArray, 0, 1)

    # i = 0
    # j = 0
    # while j < fifoArray.size / 2:
    #     currentTrack = cScanTestArray[ : ,i]
    #     nextTrack = fifoArray[ : ,j]

    #     if nextTrack[1] >= currentTrack[1]:
    #         cScanTestArray[0,i+1] = nextTrack[0]
    #         cScanTestArray[1,i+1] = nextTrack[1]
    #         fifoArray = np.delete(fifoArray, j, 1)
    #         i += 1
    #     else:
    #         j += 1
    # fifoArray = fifoArray[:, fifoArray[1, :].argsort()]

    # # Add remaining values to the new Scan array in correct order
    # j = 0
    # while j < fifoArray.size / 2:
    #     cScanTestArray[0,i+1] = fifoArray[0,j]
    #     cScanTestArray[1,i+1] = fifoArray[1,j]
    #     j += 1
    #     i += 1

    cScanTestArray = scheduleConversion(fifoArray, "cscan")

    print("The cScan max wait time is", maxWait(cScanTestArray))

    return fairnessTest(fifoCopy, cScanTestArray)

testArray = randomGen(20)

print(fifoTest(testArray))

# sstfTest

print("Scan traversed tracks and Fairness are: ", scanTest(testArray))

print("C-scan traversed tracks and Fairness are: ", cScanTest(testArray))