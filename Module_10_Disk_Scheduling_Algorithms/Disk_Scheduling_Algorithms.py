import numpy as np
from array import array
import random
import matplotlib.pyplot as plt
import statistics


def randomGen(qty: int) -> array:
    # Create uniform distribution of numbers between 0 and 99
    randomNumbs = np.random.randint(0,99,size=qty)
    print(randomNumbs)
    return randomNumbs

def scheduleConversion(fifoArray: array, scheduleType: str) -> array:
    # Create a new array to hold new schedule Array
    newArray = np.zeros((2,int(fifoArray.size/2)), dtype=int)

    # First value is first no matter schedule, therefore place first value in new array
    newArray[ : ,0] = fifoArray[ : ,0]
    fifoArray = np.delete(fifoArray, 0, 1) # delete no longer needed values

    i = 0
    j = 0
    # Loop through values to determine the upward pass based on track number
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
    
    # Conditional to sort remaining tracks for next pass in correct order
    if scheduleType == "scan":
        fifoArray = fifoArray[:, fifoArray[1, :].argsort()[::-1]] # sort descending for scan
    elif scheduleType == "cscan":
        fifoArray = fifoArray[:, fifoArray[1, :].argsort()] # sort ascending for c-scan

    # Add remaining values to the new array
    j = 0 # Not resetting i b/c we need it where it left off for indexing purposes
    while j < fifoArray.size / 2:
        newArray[0,i+1] = fifoArray[0,j]
        newArray[1,i+1] = fifoArray[1,j]
        j += 1
        i += 1

    return newArray

def fairnessTest(initArray: array, testArray: array, type: str) -> tuple:
    traversedTracks = 0
    fairnessScore = 0
    delayArray = np.empty((2,0), dtype=int)
    i = 0
    while i < testArray.size / 2 - 1:
        currentTrack = testArray[1, i]
        nextTrack = testArray[1, i+1]
        # Measure traversed tracks 
        traversedTracks = traversedTracks + abs(nextTrack - currentTrack)

        # Determine fairness by subtracting original index value from new
        # Both delayed and accelerated are included for fairness value
        fairnessScore = fairnessScore + testArray[0,i] - initArray[0,i]

        # Only delayed tracks are used for plots
        if testArray[0,i] - initArray[0,i] > 0:
            appendValues = np.array([[testArray[0,i]],[testArray[1,i]]])
            delayArray = np.append(delayArray, appendValues, axis=1)

        i += 1

    # fairnessScore = 0
    # i = 0
    # delayArray = np.empty((2,0), dtype=int)

    # while i < initArray.size / 2 - 1:
        # fairnessScore = fairnessScore + testArray[0,i] - initArray[0,i]

        # if testArray[0,i] - initArray[0,i] > 0:
        #     appendValues = np.array([[testArray[0,i]],[testArray[1,i]]])
        #     delayArray = np.append(delayArray, appendValues, axis=1)
        # i += 1

    # Plot the results of delays
    plt.bar(delayArray[1,: ], delayArray[0,: ])
    plt.xlabel('Range')
    plt.ylabel('Extent of Delay')
    if type == "scan":
        plt.title('Scan Delay Times')
    elif type == "cscan":
        plt.title('C-Scan Delay Times')
    plt.xlim(0,100)
    plt.show()

    return traversedTracks, fairnessScore

def maxWait(testArray: array) -> int:
    i = 0
    maxWaitList = []
    avgWaitList = []
    while i < testArray.size / 2 - 1:
        currentTrack = testArray[0, i]
        nextTrack = testArray[0, i+1]

        maxWaitList.append(nextTrack - currentTrack)
        i += 1

    maxWait = max(maxWaitList)
    avgWaitList = [item for item in maxWaitList if item > 0]
    avgWait = statistics.mean(avgWaitList)

    return maxWait, avgWait

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
    # Create a copy of the original array for fairness assessment
    idx = np.arange(0, fifoArray.size, 1)
    fifoArray = np.vstack((idx, fifoArray))
    fifoCopy = np.copy(fifoArray)

    # Call function to modify the FIFO array to Scan
    scanTestArray = scheduleConversion(fifoArray, "scan")
    # Call function to assess max and average wait
    print("The Scan max and average wait times are", maxWait(scanTestArray))

    # Returns results of function that creates plots and 
    return fairnessTest(fifoCopy, scanTestArray, 'scan')

def cScanTest (fifoArray: array) -> tuple:
    # Create a copy of the original array for fairness assessment
    idx = np.arange(0, fifoArray.size, 1)
    fifoArray = np.vstack((idx, fifoArray))
    fifoCopy = np.copy(fifoArray)

    cScanTestArray = scheduleConversion(fifoArray, "cscan")

    print("The C-Scan max and average wait times are", maxWait(cScanTestArray))

    return fairnessTest(fifoCopy, cScanTestArray, 'cscan')

#Call function to generate test data
testArray = randomGen(10)

print("The FIFO traversed tracks are ", fifoTest(testArray))

# sstfTest

# Call function to convert FIFO array to C-Scan schedule
print("Scan traversed tracks and Fairness are: ", scanTest(testArray))

# Call function to convert FIFO array to C-Scan schedule
print("C-scan traversed tracks and Fairness are: ", cScanTest(testArray))