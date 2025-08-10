#sum using recursion 39
# def recursiveSum(arr):
#     if not arr: 
#         return 0
#     return arr[0] + recursiveSum(arr[1:])

# print(recursiveSum([1, 2, 3, 4, 5]))
def sum(xs, i=0, s=0):
  return s if i >= len(xs) else sum(xs, i+1, s+xs[i])
print(sum([1,2,3,4]))