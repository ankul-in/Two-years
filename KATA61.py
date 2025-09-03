#kata
#https://www.codewars.com/kata/573f5c61e7752709df0005d2/train/python
def merge_arrays(first, second): 
    for i in first:
        second.append(i)
    return sorted(set(second))
    