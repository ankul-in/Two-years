#sliding window grind  
#163

# def maxSum(arr, k):
    
#     # length of the array
#     n = len(arr)

#     # n must be greater than k
#     if n <= k:
#         print("Invalid")
#         return -1

#     # Compute sum of first window of size k
#     window_sum = sum(arr[:k])

#     # first sum available
#     max_sum = window_sum

#     # Compute the sums of remaining windows by
#     # removing first element of previous
#     # window and adding last element of
#     # the current window.
#     for i in range(n - k):
#         window_sum = window_sum - arr[i] + arr[i + k]
#         max_sum = max(window_sum, max_sum)

#     return max_sum


# if __name__ == "__main__":
#     arr = [5, 2, -1, 0, 3]
#     k = 3
#     print(maxSum(arr, k))



# def maxSum(arr,k):
#     n=len(arr)
#     if n <=k:
#         print("Invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     max_sum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         max_sum=max(windowSum,max_sum)
#     return max_sum

# if __name__=="__main__":
#     arr=[5,2,-1,0,3]
#     k=3
#     print(maxSum(arr,k))


# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# if __name__=="__main__":
#     arr=[1,3,4,5,6,7,8,2]
#     k=4
#     print(maxSum(arr,k))


# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# if __name__=="__main__":
#     arr=[1,3,4,2,6,-4,-6]
#     k=4
#     print(maxSum(arr,k))

#i  can make sense of this now 

# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# if __name__=="__main__":
#     arr=[1,3,5,7,9]
#     k=3
#     print(maxSum(arr,k))

# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# if __name__=="__main__":
#     arr=[1,2,3,4,5,6,7]
#     k=2
#     print(maxSum(arr,k))

# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
# #     return maxSum
# if __name__=="__main__":
#     arr=[1,0,-9,-6,-3,2]
#     k=4
#     print(maxSum(arr,k))


# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# if __name__=="__main__":
#     arr=[1,5,3,0,-2,-5,5]
#     k=5
#     print(maxSum(arr,k))



# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# if __name__=="__main__":
#     arr=[0,7,2,-5,0,-5]
#     k=3
#     print(maxSum(arr,k))



# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# if __name__=="__main__":
#     arr=[1,6,-2,0,-5]
#     k=1
#     print(maxSum(arr,k))


# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# if __name__=="__main__":
#     arr=[1,7,4,8,2]
#     k=3
#     print(maxSum(arr,k))



# def maxSum(arr,k):
#     n=len(arr)
#     if n<=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# print(maxSum([1,5,3,2,6],5))



# def maxSum(arr,k):
#     n=len(arr)
#     if n <=k:
#         print("invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# print(maxSum([6,4,3,7,2,7],3))

# def maxSum(arr,k):
#     n=len(arr)
#     if n <= k:
#         print("Invalid")
#         return -1
#     windowSum=sum(arr[:k])
#     maxSum=windowSum
#     for i in range(n-k):
#         windowSum=windowSum-arr[i]+arr[i+k]
#         maxSum=max(windowSum,maxSum)
#     return maxSum
# print(maxSum([1,6,-4,-99,7],3))

def maxSum(arr,k):
    n=len(arr)
    if n<=k:
        print("invalid")
        return -1
    windowSum=sum(arr[:k])
    maxSum=windowSum
    for i in range(n-k):
        windowSum=windowSum-arr[i]+arr[i+k]
        maxSum=max(windowSum,maxSum)
    return maxSum

print(maxSum([5,7,-3,2,6,7],6))