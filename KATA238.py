#kata
#https://www.codewars.com/kata/55c606e6babfc5b2c500007c/solutions/python

def filter_numbers(string):

    return "".join(x for x in string if not x.isdigit())