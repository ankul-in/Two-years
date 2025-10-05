#kata
#https://www.codewars.com/kata/66c9186bb01defccbd40449d/train/python


import math
def gould(n):
    return [math.log2(2 ** bin(i).count('1')) for i in range(n + 1)]

print(gould(5))