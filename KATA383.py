#kata
#https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

def binary_array_to_number(arr):
    arr=[str(i) for i in arr]
    return int("".join(arr),2)