#kata
#https://www.codewars.com/kata/57d0089e05c186ccb600035e/train/python

import math
def equable_triangle(a,b,c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return math.isclose(area, perimeter)

