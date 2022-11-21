from array import array
import numbers
import random
from statistics import mean
import numpy as np


def arrTimeGen(low: int, k: int, size: int) -> array:
    arrivalTimeArr = np.random.randint(low, k, size)
    return arrivalTimeArr

def cpuTimeGen(d: float, v: float, size: int) -> array:
    cpuTimeArr = np.random.normal(d, v, size)
    return cpuTimeArr

def activeProcess(thisArray: array, time: int) -> array:
    for process in thisArray:
        if time >= process[0]:
            process[2] = 1
    return thisArray

def fifoQueue(k: int, d: int, v: float, n: int) -> list:
    ttList = []
    t = 0
    
    # Create an empty array to hold the sim results
    simArray = np.empty((1,n))

    # Create a zero array to be the flag value
    zeroArray = np.zeros((1,n),float)

    cpuTimeArr = cpuTimeGen(d,v,n)
    # Sort the array by arrival time for FIFO
    arrTimeArr = np.sort(arrTimeGen(0,k,n))

    # Merges the two arrays and transposes the result, effectively assigning a CPU time to an arrival time
    simArray = np.vstack((arrTimeArr, cpuTimeArr, zeroArray)).T

    for process in simArray:
        while t < process[0]:
            t += 1
            simArray = activeProcess(simArray, t)

        i = process[1]
        while i > 0:
            t += 1
            simArray = activeProcess(simArray, t)
            i -= 1
        # Set flag to inactive
        process[2] = 0
        
        ttList.append(t - process[0])
        avg_tt = round(mean(ttList),2)
        # Delete the process from the array once it has completed
        simArray = np.delete(simArray,0,0)
    return avg_tt

def sjfQueue(k: int, d: int, v: float, n: int) -> list:
    ttList = []
    t = 0
    
    # Create an empty array to hold the sim results
    simArray = np.empty((1,n))

    # Create a zero array to be the flag value
    zeroArray = np.zeros((1,n),float)

    # Get arrays for arrival time and cpu time, but sorted for SJF
    arrTimeArr = np.sort(arrTimeGen(0,k,n))
    cpuTimeArr = np.sort(cpuTimeGen(d,v,n))
    

    # Merges the two arrays and transposes the result, effectively assigning a CPU time to an arrival time
    simArray = np.vstack((arrTimeArr, cpuTimeArr, zeroArray)).T

    for process in simArray:
        while t < process[0]:
            t += 1
            simArray = activeProcess(simArray, t)

        i = process[1]
        while i > 0:
            t += 1
            simArray = activeProcess(simArray, t)
            i -= 1
        # Set flag to inactive
        process[2] = 0

        ttList.append(t - process[0])
        avg_tt = round(mean(ttList),2)
        # avg_ttList.append(avg_tt)
        # Delete the process from the array once it has completed
        simArray = np.delete(simArray,0,0)

    return avg_tt

def srtQueue(k: int, d: int, v: float, n: int) -> list:
    ttList = []
    t = 0
    
    # Create an empty array to hold the sim results
    simArray = np.empty((1,n))

    # Create a zero array to be the flag value
    zeroArray = np.zeros((1,n),float)

    # Sort the array by cpu Time time for SRT
    cpuTimeArr = np.sort(cpuTimeGen(d,v,n))
    # cpuTimeArr = np.sort(cpuTimeArr)[::-1]
    arrTimeArr = np.sort(arrTimeGen(0,k,n))

    # Merges the two arrays and transposes the result, effectively assigning a CPU time to an arrival time
    simArray = np.vstack((arrTimeArr, cpuTimeArr, zeroArray)).T

    for process in simArray:
        while t < process[0]:
            t += 1
            simArray = activeProcess(simArray, t)

        i = process[1]
        while i > 0:
            t += 1
            simArray = activeProcess(simArray, t)
            i -= 1
        # Set flag to inactive
        process[2] = 0

        ttList.append(t - process[0])
        avg_tt = round(mean(ttList),2)
        # avg_ttList.append(avg_tt)
        # Delete the process from the array once it has completed
        simArray = np.delete(simArray,0,0)

    return avg_tt

j = 0
k = 1000
d = 20
v = 0.05 * d
n = 100
avg_ttList = []
while j < 100:
    avg_ttList.append(fifoQueue(k,d,v,n))
    j += 1
print(avg_ttList)

j = 0
avg_ttList = []
while j < 100:
    avg_ttList.append(sjfQueue(k,d,v,n))
    j += 1
print(avg_ttList)

j = 0
avg_ttList = []
while j < 100:
    avg_ttList.append(srtQueue(k,d,v,n))
    j += 1
print(avg_ttList)