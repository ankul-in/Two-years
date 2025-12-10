#kata
#https://www.codewars.com/kata/589b1c15081bcbfe6700017a/train/python

import math
def cost(min):
    if min <= 65:
        return 30
    extra_time = min - 60
    extra_time = max(0, extra_time - 5)
    half_hours = math.ceil(extra_time / 30)
    return 30 + half_hours * 10

