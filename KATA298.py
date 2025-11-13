#kata
#https://www.codewars.com/kata/5870db16056584eab0000006/train/python

import math
def get_score(x,y):
    r = math.hypot(x, y)
    sector_angles = [
        6, 13, 4, 18, 1, 20, 5, 12, 9, 14,
        11, 8, 16, 7, 19, 3, 17, 2, 15, 10
    ]
    angle = math.degrees(math.atan2(y, x))
    if angle < 0:
        angle += 360
    sector_index = int(((angle + 9) % 360) // 18)
    score = sector_angles[sector_index]
    if r > 170:  
        return "X"
    elif r <= 6.35:
        return "DB"
    elif r <= 15.9:
        return "SB"
    elif 99 <= r <= 107:
        return f"T{score}"
    elif 162 <= r <= 170:
        return f"D{score}"
    else:
        return str(score)