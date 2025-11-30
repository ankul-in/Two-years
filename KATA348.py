#kata
#https://www.codewars.com/kata/57d2ba8095497e484e00002e/train/python

import string
def borrow(s):
    s = "".join(s.lower().split(" "))
    s = ''.join(ch for ch in s if ch not in string.punctuation)
    return s


