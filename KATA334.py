#kata
#https://www.codewars.com/kata/554b4ac871d6813a03000035/solutions/python

def high_and_low(numbers):
    num=[int(i) for i in numbers.split(" ")]
    return "{} {}".format(max(num),min(num))