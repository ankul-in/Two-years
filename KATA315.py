#kata
#https://www.codewars.com/kata/52988f3f7edba9839c00037d/train/python

def reject(seq, predicate): 
    return [item for item in seq if not predicate(item)]