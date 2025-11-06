#kata
#https://www.codewars.com/kata/58f6f87a55d759439b000073/train/python

def negation_value(s: str, val) -> bool:
    base = bool(val)
    return base if len(s) % 2 == 0 else not base

