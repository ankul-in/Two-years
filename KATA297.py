#kata
#https://www.codewars.com/kata/59e0dbb72a7acc3610000017/train/python

from math import gcd
def coprimes(n):
    return sorted(k for k in range(1, n) if gcd(n, k) == 1)