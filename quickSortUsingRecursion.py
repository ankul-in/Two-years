#pivot sort or quick sort using recursion
arr=[]
def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        leftArr=[]
        rightArr=[]
        for i in arr[1:]:
            if i>pivot:
                rightArr.append(i)
            else:
                leftArr.append(i)
        newArr=quickSort(leftArr) + [pivot] +quickSort(rightArr)
        return newArr
    
print(quickSort([6,5,4,7,8,2,9,1,3]))
                
    #hell yeah on second try