#kata
#https://www.codewars.com/kata/5734c38da41454b7f700106e/train/python

from collections import Counter
def only_one(*args):
    bools=[*args]
    counts=Counter(bools)
    return 1 == counts[True]
