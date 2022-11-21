# Banker's Algorithm by Chip Henderson for CS7343

from array import array
import numpy as np


def initProcesses(p: int, r: int) -> array:
    # Section provides hardcoded values for quick test matching zyBook example
    # maxClaimArr = [[2,1],[2,2],[2,2]]
    # allocArr = [[0,1],[0,0],[0,2]]
    # reqArr = [[1,0],[1,0],[1,0]]

    # *****Comment out section below for hard coded test*****
    # """
    # Create empty separate arrays based on user input
    maxClaimArr = np.zeros((p, r), int)
    allocArr = np.zeros((p, r), int)
    reqArr = np.zeros((p, r), int)

    # Collect user inputs to populate each value of array
    i = 0
    j = 0
    while j < p:
        while i < r:
            maxClaimArr[j, i] = input(
                f"\nEnter max number of claims for process {j + 1}, resource {i + 1}: ")
            i += 1
            # print(maxClaimArr) # Debug
        j += 1
        i = 0

    i = 0
    j = 0
    while j < p:
        while i < r:
            allocArr[j, i] = input(
                f"\nEnter current allocations for process {j + 1}, resource {i + 1}: ")
            i += 1
        j += 1
        i = 0

    i = 0
    j = 0
    while j < p:
        while i < r:
            reqArr[j, i] = input(
                f"\nEnter current requests for process {j + 1}, resource {i + 1}: ")
            i += 1
        j += 1
        i = 0
    # """
    # *****Comment out section above for hard coded test*****

    # Merge the three arrays into one
    bankerArr = np.hstack((maxClaimArr, allocArr, reqArr))

    return bankerArr


def initResources(r: int) -> array:
    # availArr = np.array([2,0]) # Uncomment for faster hardcoded test

    # *****Comment out section below for hard coded test*****
    # """"
    # Establish the resources array
    availArr = np.zeros((r,), int)

    # Collect data from the user to populate the number of units for each resource
    i = 0
    while i < r:
        availArr[i] = input(f"\nEnter number of units for resource {i + 1}: ")
        i += 1
    # """
    # *****Comment out section above for hard coded test*****
    return availArr


def bankerTest(processTest: array, availTest: array):
    resourceShape = availTest.shape

    # Loop through affected process values, check for validity
    i = 0
    while i < resourceShape[0]:
        if processTest[i] - processTest[i+2] > availTest[i]:
            print("New state rejected")
            return
        i += 1

    print("New state accepted")
    return


def request(i: int, j: int, k: int):
    # Create temporary arrays for testing so originals are not altered
    tempProcess = processArr
    tempAvail = resourceArr

    tempProcess[i-1, j+1] = tempProcess[i-1, j+1] + \
        k  # Increase current allocation
    tempProcess[i-1, j+3] = tempProcess[i-1, j+3] - \
        k  # Decrease current requests

    tempAvail[j-1] = tempAvail[j-1] - k  # Decrease available units

    # Call function to perform Banker's Algorithm test
    bankerTest(tempProcess[i-1], tempAvail)

    return


def release(i: int, j: int, k: int):
    # Create temporary arrays for testing so originals are not altered
    tempProcess = processArr
    tempAvail = resourceArr

    tempProcess[i-1, j+1] = tempProcess[i-1, j+1] - k
    tempProcess[i-1, j+3] = tempProcess[i-1, j+3] + k

    tempAvail[j-1] = tempAvail[j-1] + k

    bankerTest(tempProcess[i], tempAvail)

    return


def bankersAlgorithm():
    i = 0  # Process value
    j = 0  # Resource Value
    k = 0  # Number of units
    global exit

    userInput = input("Enter request, release, or exit: ")

    if userInput == "request":
        i, j, k = input(
            "Enter request values as integers process number, resource number, number of units ").split()
        # Call function to implement request changes
        request(int(i), int(j), int(k))
    elif userInput == "release":
        i, j, k = input(
            "Enter release values as integers process number, resource number, number of units ").split()
        # Call function to implement release changes
        release(int(i), int(j), int(k))
    elif userInput == "exit":
        exit = True

    return


# Prompt user for the number of processes and resources
processes = input("Enter the number of Processes: ")
resources = input("Enter the number of resources: ")

# Uncomment following two lines for hardcoded testing
# processes = 3
# resources = 2

# Call function to establish initial processes array
processArr = initProcesses(int(processes), int(resources))
print(f"Starting process array\n{processArr}")

# Call function to establish initial units per resource array
resourceArr = initResources(int(resources))
print(f"Starting resource array\n{resourceArr}")

# Controls game play once initial arrays are established
exit = False
while exit == False:
    bankersAlgorithm()
