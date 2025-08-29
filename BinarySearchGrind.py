#binarySearch 
def binarySearch(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1


arr=[2,3,4,10,40]
x=10
result=binarySearch(arr,x)
if result !=-1:
    print("element is present at index-", result)
else:
    print("enement no present in array")




#recursive binary search

def binarySearch(arr,low,high,x):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,low,mid-1,x)
        else:
            return binarySearch(arr,mid+1,high,x)
    else:
        return -1
result=binarySearch(arr,0,len(arr)-1,x)
if result != -1:
    print(result)
else:
    print("Enement not in array")