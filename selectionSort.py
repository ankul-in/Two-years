
def arrayInput():
    arr=[]
    n=int(input("enter number of digits in array"))
    for i in range(n):
        x=int(input("enter digit-->"))
        arr.append(x)
    return arr
def smallestInArray(arr):
    smallest=arr[0]
    smallestIndex=0
    for i in range(len(arr)):
        if smallest>arr[i]:
            smallest=arr[i]
            smallestIndex=i
    return smallestIndex
arr=arrayInput()
def selectionSort(arr):
    n=len(arr)

    newArr=[]
    for i in range(n):
        smallest=smallestInArray(arr)
        x=arr.pop(smallest)
        newArr.append(x)
    return newArr

print(selectionSort(arr))

    
#smallestInArray(array)
# biggestInArray(array)
