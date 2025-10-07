#kata
#https://www.codewars.com/kata/595877be60d17855980013d3/train/python

import math

def euclidean_distance(p1,p2):
    return round(math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2))),2)

#well well well
from math import dist

def euclidean_distance(point1, point2):
    return round(dist(point1, point2), 2)