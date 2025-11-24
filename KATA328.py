#kata
#https://www.codewars.com/kata/58dceee2c9613aacb40000b9/train/python
class Point():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

import math
def distance_between_points(a: Point, b: Point) -> float:
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2)


# print(distance_between_points(Point(1, 3, 5), Point(1, 3, 5)))