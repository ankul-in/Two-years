#kata
#https://www.codewars.com/kata/58e3e62f20617b6d7700120a/train/python

import math
def distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

def triangle_perimeter(triangle):
    perimeter=(distance(triangle.a,triangle.b)+distance(triangle.b,triangle.c)+distance(triangle.c,triangle.a))
    return perimeter