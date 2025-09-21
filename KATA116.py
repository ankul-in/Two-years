#kata
#https://www.codewars.com/kata/520d9c27e9940532eb00018e/train/python

def solution(*args):
    listargs=list(args)
    setargs=set(args)
    if len(listargs)!=len(setargs):
        return True
    return False