# #binarySearch 
# def binarySearch(arr,x):
#     low=0
#     high=len(arr)-1
#     while low<=high:
#         mid=low+(high-low)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]<x:
#             low=mid+1
#         else:
#             high=mid-1


arr=[2,3,4,10,40]
x=10
# result=binarySearch(arr,x)
# if result !=-1:
#     print("element is present at index-", result)
# else:
#     print("enement no present in array")




#recursive binary search

# def binarySearch(arr,low,high,x):
#     if high>=low:
#         mid=low+(high-low)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             return binarySearch(arr,low,mid-1,x)
#         else:
#             return binarySearch(arr,mid+1,high,x)
#     else:
#         return -1
# result=binarySearch(arr,0,len(arr)-1,x)
# if result != -1:
#     print(result)
# else:
#     print("Enement not in array")



####################################################################################################


# def binarySearch(arr,x):
#     low , high = 0,len(arr)-1
#     while low<=high:
#         mid=low+(high-low)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]<x:
#             low=mid+1
#         elif arr[mid]>x:
#             high=mid-1
#     return -1
# print(binarySearch(arr,10))


# def binarySearch(arr,x):
#     low,high=0,len(arr)-1
#     while low<=high:
#         mid=low+(high-low)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             high=mid-1
#         elif arr[mid]<x:
#             low=mid+1
#     return -1

# print(binarySearch(arr,2))


def binarySearch(arr,x):
    low,high=0,len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
    return -1
<<<<<<< HEAD
print(binarySearch(arr,33))
=======
print(binarySearch(arr,33))
>>>>>>> c2598b151217cfee673986a5c48752d5c5de5d96
