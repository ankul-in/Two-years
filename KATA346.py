#kata
#https://www.codewars.com/kata/5a106ce7ffe75f4c200000f7/train/python

import random
def find_random_seed(lst):
    for i in range(10000):
        random.seed(i)
        if lst==[random.randint(0, 100) for _ in range(10)]:
            return i
    
