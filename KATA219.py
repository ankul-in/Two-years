#kata
#https://www.codewars.com/kata/559aa1295f5c38fd7b0000ac/python

import math
def routes(n):
    if n>0:
        return math.comb(2*n,n)
    return 0

#good stuff math.comb

from math import factorial

def routes(n):
    return n > 0 and factorial(2*n) // factorial(n)**2
#good stuff factorial