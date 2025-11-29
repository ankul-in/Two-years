#kata
#https://www.codewars.com/kata/5adadcb36edb07df5600092e/train/python

def seven_wonders_science(compasses, gears, tablets):
    set_points = 7 * min(compasses, gears, tablets)
    square_points = compasses**2 + gears**2 + tablets**2
    return set_points + square_points


