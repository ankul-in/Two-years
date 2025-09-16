#kata
#https://www.codewars.com/kata/58d3487a643a3f6aa20000ff/train/python
def min_min_max(arr):
    for i in range(min(arr)+1,max(arr)):
        if i not in arr:
            minimumAbsent=i
            break
    return [min(arr),minimumAbsent,max(arr)]

"""def minMinMax(arr):
    s, mi, ma = set(arr), min(arr), max(arr)
    return [mi, next(x for x in range(mi+1, ma) if x not in s), ma]"""