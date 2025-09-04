#kata
#https://www.codewars.com/kata/5862f663b4e9d6f12b00003b/train/python
#probablility of blue out of total remaining


def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    blue=blue_start-blue_pulled
    red=red_start-red_pulled
    total=blue+red
    pBlue=blue/total
    
    return pBlue