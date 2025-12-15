#kata
#https://www.codewars.com/kata/54599705cbae2aa60b0011a4/train/python

def one(xs, f): 
    count = sum(1 for item in xs if f(item))
    return count == 1
