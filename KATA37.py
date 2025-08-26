def even_odd(arr):
    while len(arr)>=2:
        x=arr[0]*arr[1]
        arr.pop(0)
        arr.pop(0)
        arr.insert(0,x)

        if len(arr)>=2:
            y=arr[0]+arr[1]
            arr.pop(0)
            arr.pop(0)
            arr.insert(0,y)

    return arr.pop()




print(even_odd([1,2,3]))
print(even_odd([3,0]))