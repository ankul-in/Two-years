#kata
#https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python


import math

def easyline(n):
    total = 0
    for k in range(n + 1):
        binom = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        total += binom * binom  
    return total