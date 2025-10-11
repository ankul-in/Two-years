#kata
#https://www.codewars.com/kata/528d9adf0e03778b9e00067e/train/python

def mine_location(field):
    for row_index, row in enumerate(field):
        for col_index, cell in enumerate(row):
            if cell == 1:
                return [row_index, col_index]
    return -1

print(mine_location([ [1, 0], [0, 0] ]))

#hell yeah
from numpy import where, array

def mineLocation(field):
    x, y = where(array(field) == 1)
    return [int(x), int(y)]