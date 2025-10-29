#kata
#https://www.codewars.com/kata/57e17750621bca9e6f00006f/train/python

color_map = {
        (0,): 'red',
        (1,): 'green',
        (2,): 'blue',
        (0, 1): 'yellow',
        (1, 2): 'cyan',
        (0, 2): 'magenta',
        (0, 1, 2): 'white'
    }
def hex_color(codes):
    if not codes:
        return "black"
    x = [int(i) for i in codes.split()]
    if x == [0, 0, 0]:
        return 'black'
    max_val = max(x)
    y = [i for i, val in enumerate(x) if val == max_val]
    return color_map.get(tuple(sorted(y)), 'unknown')