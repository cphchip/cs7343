import numpy as np
from array import array
import random

def randomGen(qty: int) -> array:
    randomNumbs = np.random.randint(0,10,size=qty)
    print(randomNumbs)
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
    j = 0
    traversedTracksScan = 0
    passedTracks = []

    secondPass = np.empty(1, dtype=int)
    # print(secondPass)


    while i < testNumbs.size - 1: 
        currentTrack = testNumbs[i]
        nextTrack = testNumbs[i + 1]
         
        # something = len(passedTracks)        

        if nextTrack > currentTrack:
            traversedTracksScan = nextTrack - currentTrack
            # testNumbs = np.delete(testNumbs,i)
            i += 1
            # j += 1
        elif nextTrack <= currentTrack:
            # np.insert(secondPass, int, nextTrack)
            # secondPass[j] = nextTrack
            passedTracks.append(nextTrack)
            testNumbs = np.delete(testNumbs,i+1)
        
        secondPass = np.array(passedTracks)
        secondPass.sort()

    # Can I do this just by sorting the remaining array for the backward pass?
    # testNumbs.sort()
    i = secondPass.size - 1
    while i > -1:
        currentTrack = secondPass[i]
        nextTrack = secondPass[i - 1]
        
        traversedTracksScan = traversedTracksScan + abs(nextTrack - currentTrack)

        i -= 1

    return traversedTracksScan


testArray = randomGen(10)

# randomGen(100)

print(fifoTest(testArray))

# sstfTest

print(scanTest(testArray))

# cScanTest