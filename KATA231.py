#kata
#https://www.codewars.com/kata/559cc2d2b802a5c94700000c/train/python

def consecutive(arr):
    if not arr:
        return 0
    return max(arr)-min(arr)-(len(arr)-1)