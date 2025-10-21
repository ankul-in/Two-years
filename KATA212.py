#kata
#https://www.codewars.com/kata/59f11118a5e129e591000134/train/python

from collections import Counter
def repeats(arr):
    count=Counter(arr)
    return sum([i for i,j in count.items() if j<=1])

print(repeats([5, 17, 18, 11, 13, 18, 11, 13]))

def repeats(arr):
    return sum([x for x in arr if arr.count(x) == 1])