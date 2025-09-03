#kata
#https://www.codewars.com/kata/594093784aafb857f0000122
def diff(a, b):
    return sorted(set(a)^set(b))
def diff(a,b):
    x=set(a)
    y=set(b)
    return sorted(list(x^y))
def diff(a,b):
    return set(a).symmetric_difference(set(b))


