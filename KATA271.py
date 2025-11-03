#kata
#https://www.codewars.com/kata/553e8b195b853c6db4000048/train/python

def has_unique_characters(s):
    if len(s) > 128:
        return False
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

