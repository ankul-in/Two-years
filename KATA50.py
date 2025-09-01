#https://www.codewars.com/kata/5b4e474305f04bea11000148/train/python
#kata

from itertools import combinations

def digits(num):

    num=str(num)
    sumsList=list(num)
    comb = combinations(sumsList,2)
    return print([int(a)+int(b) for a,b in list(comb)])


digits(156)