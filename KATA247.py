#kata
#https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095/train/python

def max_diff(lst):
    if not lst: return 0
    return max(lst)-min(lst)