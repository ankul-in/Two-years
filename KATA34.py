#kata https://www.codewars.com/kata/56cafdabc8cfcc3ad4000a2b/train/python

def score(n):
    result=0
    for i in range(n):
        result|=(i+1)
    return result


def score(n):
    r=1
    while r <=n:
        r<<=1
    return r-1