#wap smallest number in array
from arrayInput import arrayInput
def smallestInArray(arr):
    smallest=arr[0]
    smallestIndex=0
    for i in range(len(arr)):
        if smallest>arr[i]:
            smallest=arr[i]
            smallestIndex=i
    return print("the smallest number in array is-->",smallest,"at the index",smallestIndex)
    
