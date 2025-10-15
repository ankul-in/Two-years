#kata
#https://www.codewars.com/kata/555f43d8140a6df1dd00012b/train/python

import math
def coordinates(degrees, radius):
    radians = math.radians(degrees)

    x=radius*math.cos(radians)
    y=radius*math.sin(radians)
    return (round(x,10),round(y,10))

print(coordinates(1090,10000))