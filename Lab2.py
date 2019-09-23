#CS2302 Data Structures
#Assignment: Lab 2
#TA: Anindita Nath
#Professor: Olac Fuentes
#Purpose: To be able to implement various versions of quick sort and bubble sort

import time


def Bubble_Sort(L, n, k):
    startTime = time.time()
    #Base case will return the list and the end time
    if n < 1:
        endTime = time.time()
        return L[k - 1], endTime - startTime
    #we use a for loop to be able to make swaps
    #we use a variable n as a counter that will be used
    #to determine when we reach out base case.
    for i in range(n):
        if L[i] > L[i + 1]:
            L[i], L[i + 1] = L[i + 1], L[i]
    #the return statement is used with n-1 to be able to
    #bring us closer to our base case
    return Bubble_Sort(L, n - 1, k)

#This method helps us create a partition
#which will be used in the quick sort methods
def Partition(L, startIndex, endIndex):
    smallerElemIndex = (startIndex - 1)
    pivot = L[endIndex]
    
    for i in range(startIndex , endIndex):
        if L[i] <= pivot:
            smallerElemIndex = smallerElemIndex + 1
            L[smallerElemIndex], L[i] = L[i], L[smallerElemIndex]
    L[smallerElemIndex + 1], L[endIndex] = L[endIndex], L[smallerElemIndex + 1]
    return (smallerElemIndex + 1)
        
#This is a traditional quicksort method
def Quick_Sort(L, startIndex, endIndex, k):
    startTime = time.time()
    if startIndex < endIndex:
        #The following variable is our partitioning index,
        #which after the call is made we will know it is in
        #the correct position. 
        partIndex = Partition(L, startIndex, endIndex)
        #used for everything before our partIndex
        Quick_Sort(L, startIndex, partIndex - 1, k)
        #used for everything after our partIndex
        Quick_Sort(L, partIndex + 1, endIndex, k)
    #endTime is used to keep track of 
    #when our program is done executing
    endTime = time.time()
    #will return the elemet in the kth position
    #as well as the run time.
    return L[k - 1], endTime - startTime

#This is the modified quicksort method
def Quick_Sort_Mod(L, startIndex, endIndex, k):
    startTime = time.time()
    while(startIndex < endIndex):
        #partIndex is the same as in our traditional Quicksort
        partIndex = Partition(L, startIndex, endIndex)
        #used to sort only elements if k is in the left
        if k < int(len(L) / 2):
            Quick_Sort_Mod(L, startIndex, partIndex - 1, k)
            startIndex = partIndex + 1
        #used to sort only elements if k is in the right
        elif k > int(len(L) / 2):
            Quick_Sort_Mod(L, partIndex + 1, endIndex, k)
            endIndex = partIndex - 1
    #endTime will help us keep track of when the program is done executing
    
    endTime = time.time()
    return L[k - 1], endTime - startTime

#This quicksort method that is implemented using a stack
def Quick_Sort_Stack(L, startIndex, endIndex, k):
    startTime = time.time()
    #stack will be used as an array of arrays
    stack = [[L, startIndex, endIndex]]
   #while will run as long as our stack is not empty
    while len(stack) > 0:
        #is used to pop from the stack
        h = stack.pop(-1)
        if h[1] > h[2]:
            partIndex = Partition(h[0], h[1], h[2])
            stack.append(L, startIndex, partIndex - 1)
            stack.append(L, partIndex + 1, endIndex)
    endTime = time.time()
    return L[k -1], endTime - startTime

#L1 is an incremental list of 2500 elements
#L2 is the reverse of L1    
L1 = list(range(2500))
L2 = L1[::-1]

#Best case scenario already sorted
print(Bubble_Sort(L1, len(L1) - 1, 999))
#Worst case scenario sorted in reverse
print(Bubble_Sort(L2, len(L2) - 1, 999))

#Best case scenario is if pivot is the middle,
#worst case is if pivot is the max or min
print(Quick_Sort(L2, 0, len(L2) - 1, 1))

#Best case scenario is if pivot is the middle,
#worst case is if pivot is the max or min
print(Quick_Sort_Mod(L2, 0, len(L2) - 1, 1000))

#Best case scenario is if pivot is the middle,
#worst case is if pivot is the max or min
print(Quick_Sort_Stack(L1, 0, len(L1) - 1, 1))