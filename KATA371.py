#kata
#https://www.codewars.com/kata/5a805631ba1bb55b0c0000b8/train/python

def case_sensitive(s):
    upper = [ch for ch in s if ch.isalpha() and not ch.islower()]
    return [len(upper) == 0, upper]
