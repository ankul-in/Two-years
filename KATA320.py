#kata
#https://www.codewars.com/kata/58989a079c70093f3e00008d/train/python

def cartesian_neighbor(x, y):
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]
    neighbors = [(x + dx, y + dy) for dx, dy in offsets]
    return neighbors

