#kata
#https://www.codewars.com/kata/585b1fafe08bae9988000314/train/python

def explode(s):
    result = []
    for ch in s:
        digit = int(ch)
        result.append(ch * digit)
    return "".join(result)
