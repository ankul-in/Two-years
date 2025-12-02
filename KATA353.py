#kata
#https://www.codewars.com/kata/56d3e702fc231fdf72001779/train/python

def sxore(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:  
        return 0