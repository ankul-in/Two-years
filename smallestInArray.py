#wap smallest number in array
def smallestInArray(arr):
    smallest=arr[0]
    smallestIndex=0
    for i in range(len(arr)):
        if smallest>arr[i]:
            smallest=arr[i]
            smallestIndex=i
    print("the smallest number in array is-->",smallest,"at the index",smallestIndex)
arr=[]
n=int(input("enter number of digits in array"))
for i in range(n):
    x=int(input("enter digit-->"))
    arr.append(x)
smallestInArray(arr)