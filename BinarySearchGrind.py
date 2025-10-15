# #binarySearch  #145
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


# arr=[2,3,4,10,40]
# x=10
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
# print(binarySearch(arr,33))



# def binarySearch(arr,x):
#     low,high=0,len(arr)-1
#     while low<=high:
#         mid=low+(high-low)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             high=mid-1
#         else:
#             low=mid+1
#     return -1

# print(binarySearch(arr,3))


# def binarySearch(arr,x):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             end=mid-1
#         else:
#             start=mid+1
#     return -1
# print(binarySearch(arr,2))



# def binarySearch(arr,x):
#     first,last=0,len(arr)-1
#     while first <=last:
#         mid=first+(last-first)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             first=mid+1
#         else:
#             last=mid-1
#     return 1

# print(binarySearch(arr,2))

# i dont think ima ever forget binary search tho


# def binarySearch(arr,x):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]<x:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1

# print(binarySearch(arr,5))

#sorry i forgot the number
#yeah



# def binarySearch(arr,low,high,x):
#     if high<low:
#         return -1
#     mid=low+(high-low)//2
#     if arr[mid]==x:
#         return mid
#     elif arr[mid]>x:
#         return binarySearch(arr,low,mid-1,x)
#     elif arr[mid]<x:
#         return binarySearch(arr,mid+1,high,x)
    
# print(binarySearch(arr,0,len(arr)-1,10))




# def binarySearch(arr,x):
#     front,back=0,len(arr)-1
#     while front <= back:
#         mid=front+(back-front)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             back=mid-1
#         else:
#             front=mid+1
#     return -1

# print(binarySearch([1,2,3,4,5,6,7,8,9],9))


# def binarySearch(arr,x):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]<x:
#             start=mid+1
#         elif arr[mid]>x:
#             end=mid-1
#     return -1

# print(binarySearch([1,2,3,4,5,6,7,8],6))

#yeah i kinda get this now 

# def binarySearch(arr,k):
#     start,finish=0,len(arr)-1
#     while start<=finish:
#         mid=start+(finish-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1

# # print(binarySearch([1,2,3,4,5,6,7,8,9],7))

# def binarySearch(arr,x):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             end=mid-1
#         else:
#             start=mid+1
#     return -1
# print(binarySearch([1,4,6,8,12,13,45,80],45))

# def binarySearch(arr,k):
#     start,finish=0,len(arr)-1
#     while start<=finish:
#         mid=start+(finish-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]>k:
#             finish=mid-1
#         else:
#             start=mid+1
#     return "error"
# print(binarySearch([1,2,3,4,5,6,7,8,9,10],5))


# def binarySearch(arr,s):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==s:
#             return mid
#         elif arr[mid]<s:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([1,3,5,7,9,11,13,15,17,19],3))

# def binarySearch(arr,s):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==s:
#             return mid
#         elif arr[mid]<s:
#             start=mid+1
#         elif arr[mid]>s:
#             end=mid-1
#     return -1
# print(binarySearch([1,3,5,6,7,8,9,11],6))

# def binarySearch(arr,k):
#     i,j=0,len(arr)-1
#     while i<j:
#         mid=i+(j-i)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             i=mid+1
#         else:
#             j=mid-1
#     return -1
# print(binarySearch([1,2,3,4,5],3))

# def binarySearch(arr,k):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([1,2,3,4,5,6],2))


# def binarySearch(arr,k):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([1,2,3,4,5,6],5))



# def binarySearch(arr,k):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12],12))





# def binarySearch(arr,k):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([1,2,3,4,5],6))



# def binarySearch(arr,k):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([1,2,3,4,5,6,7,8,9],9))




# def binarySearch(arr,k):

#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([-5,-4,-3,-2,-1],-3))


# def binarySearch(arr,k):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([1,2,3,1,2,3,1,2,3],3))


# def binarySearch(arr,k):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([1,10,100,1000,100000],100))


# def binarySearch(arr,k):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([-1000,-100,-10,-1,0,1],-10))




# def binarySearch(arr,k):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
# print(binarySearch([10,0,-10],-10))



def binarySearch(arr,k):
    start,end=0,len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            start=mid+1
        else:
            end=mid-1
    return -1
print(binarySearch([-100,-99,-98,-97,0],-97))