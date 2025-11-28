#kata
#https://www.codewars.com/kata/5cd12646cf44af0020c727dd/train/python

import math

PI_DIGITS = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def square_pi(digits):
    s = sum(int(c) ** 2 for c in PI_DIGITS[:digits])
    r = math.isqrt(s)
    return r if r * r == s else r + 1

