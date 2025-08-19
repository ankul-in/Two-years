#kata https://www.codewars.com/kata/55b1e5c4cbe09e46b3000034/train/python
#pronic number

import math
def is_pronic(n):
    if n<0:
        return False
    sqr=math.sqrt(n)
    x=int(sqr)
    if x*(x+1)==n:
        return True
    else:
        return False