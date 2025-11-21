#kata
#https://www.codewars.com/kata/5932c94f6aa4d1d786000028/train/python


def perfect_roots(n):
    root = round(n ** (1/8))
    return root ** 8 == n

