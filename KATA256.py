#kata
#https://www.codewars.com/kata/56e56756404bb1c950000992/train/python

import math

def lcm(a, b):
    if math.gcd(a,b)==0:
        return 0
    return abs(a * b) // math.gcd(a, b)

def sum_differences_between_products_and_LCMs(pairs):
    if not pairs: return 0
    answer=[]
    for i in pairs:
        answer.append((i[0]*i[1])-lcm(i[0],i[1]))
    return sum(answer)