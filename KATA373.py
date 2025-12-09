#kata
#https://www.codewars.com/kata/67a61fa0ed1d3932f2c39b66/train/python

def get_depth(arr):
    depth = 1
    while arr and isinstance(arr[0], list):
        arr = arr[0]
        depth += 1
    return depth

def sort_by_depth(lst):
    return sorted(lst, key=get_depth)

