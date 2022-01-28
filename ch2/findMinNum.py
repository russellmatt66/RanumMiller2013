"""
Matt Russell
1/27/22

Requirements:
Write two Python functions to find the minimum number in a list.
The first function should compare each number to every other number in the list: O(n^2).
The second function should be linear: O(n).
"""
def findMin_nsq(numList):
    """
    O(n^2) implementation
    ---------------------
    numList - minimum is in here 
    """
    if type(numList) != list:
        raise RuntimeError("Object must be a list!")
    else:
        pass
    wasMax = [0] * len(numList) # store how many times number was larger
    for idx in range(len(numList)):
        for jidx in range(len(numList)):
            if(numList[idx] > numList[jidx]): 
                wasMax[idx] += 1
        if(wasMax[idx] == 0): # numList[idx] was never larger
            listMinNum = numList[idx]
        else:
            pass
    return listMinNum

def findMin_n(numList):
    """
    O(n) implementation
    ---------------------
    numList - minimum is in here 
    """
    if type(numList) != list:
        raise RuntimeError("Object must be a list!")
    else:
        pass
    listMinNum = numList[0] # might as well guess first item
    for idx in range(len(numList)):
        if(numList[idx] < listMinNum):
            listMinNum = numList[idx]
        else:
            pass
    return listMinNum

"""
Test the functions
"""
from numpy import random

listLen = random.randint(10,20) # Don't want list to be too big or small
numList = []

for lidx in range(listLen):
    numList.append(random.randint(0,1000))

MinNum_nsq = findMin_nsq(numList)
MinNum_n = findMin_n(numList)

print("The list",numList,"has minimum number", MinNum_nsq)
print("The list",numList,"has minimum number", MinNum_n)
    
