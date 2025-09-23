#kata
#https://www.codewars.com/kata/5a8059b1fd577709860000f6/train/python

def alphabetic(s):
    return s == "".join(sorted(list(s)))
print(alphabetic('door'))


def alphabetic(s):
    return sorted(s) == list(s)