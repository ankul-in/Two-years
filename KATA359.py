#kata
#https://www.codewars.com/kata/567d609f1c16d7369c000008/train/python

import random
def generate(length):
    return ''.join(random.choice('01') for _ in range(length))

