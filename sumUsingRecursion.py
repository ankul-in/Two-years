#sum using recursion
def recursiveSum(arr):
    if not arr: 
        return 0
    return arr[0] + recursiveSum(arr[1:])

print(recursiveSum([1, 2, 3, 4, 5]))
