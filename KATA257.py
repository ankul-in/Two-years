#kata
#https://www.codewars.com/kata/5b7176768adeae9bc9000056/train/python

def index_equals_value(arr):
    for i,j in enumerate(arr):
        if i==j:
            return i
    return -1
