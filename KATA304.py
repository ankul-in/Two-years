#kata
#https://www.codewars.com/kata/57073869924f34185100036d/train/python

import random


def random_case(s):
    result = []
    for ch in s:
        if ch.isalpha():  
            if random.choice([True, False]):
                result.append(ch.upper())
            else:
                result.append(ch.lower())
        else:
            result.append(ch)  
    return "".join(result)

