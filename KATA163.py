#kata
#https://www.codewars.com/kata/5612a42e746aa62de100001a/train/python

import math

def db_scale(intensity):
    db=10*math.log10(intensity/(10**-12))  
    return db