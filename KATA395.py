#kata
#https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/train/python

def reverse(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10         
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
        
        