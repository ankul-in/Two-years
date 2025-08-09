#biggest in array
def biggestInArray(arr):
    biggest=arr[0]
    biggestIndex=0
    for i in range(len(arr)):
        if biggest<arr[i]:
            biggest=arr[i]
            biggestIndex=i
    
    return biggestIndex
# arr[biggestInArray]
# print("the biggest number in array is-->",biggest," at the index ",biggestIndex)
