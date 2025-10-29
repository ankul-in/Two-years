#kata251    
#https://www.codewars.com/kata/59a1cdde9f922b83ee00003b/train/python

def stanton_measure(arr):
    n=arr.count(1)
    return arr.count(n)

print(stanton_measure([1, 4, 3, 2, 1, 2, 3, 2]))