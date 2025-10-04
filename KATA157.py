#kata
#https://www.codewars.com/kata/5b01abb9de4c7f3c22000012/train/python

import math
def ellipse_contains_point(f0, f1, l, p): 
    d0 = math.hypot(p["x"] - f0["x"], p["y"] - f0["y"])
    d1 = math.hypot(p["x"] - f1["x"], p["y"] - f1["y"])
    total_distance = d0 + d1
    return total_distance <= l


print(ellipse_contains_point({ 'x': 0, 'y': 0 }, { 'x': 0, 'y': 0 }, 2, { 'x': 0, 'y': 0 }))