#sliding window grind
def maxSum(arr,k):
    n=len(arr)
    if n <=k:
        print("Invalid")
        return -1
    windowSum=sum(arr[:k])
    max_sum=windowSum
    for i in range(n-k):
        windowSum=windowSum-arr[i]+arr[i+k]
        max_sum=max(windowSum,max_sum)
    return max_sum

if __name__=="__main__":
    arr=[5,2,-1,0,3]
    k=3
    print(maxSum(arr,k))
    