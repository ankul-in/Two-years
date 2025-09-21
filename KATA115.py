#kata
#https://www.codewars.com/kata/57630df805fea67b290009a3/train/python
def encode(s):
    total = 0
    for c in s:
        total = total * 26 + (ord(c) - ord('a'))
    return total + 1

print(encode("foo"))