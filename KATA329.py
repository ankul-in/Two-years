#kata
#https://www.codewars.com/kata/5822d89270ca28c85c0000f3/train/python

def scramble(s, indices):
    result = [''] * len(s)
    for i, char in enumerate(s):
        result[indices[i]] = char
    return ''.join(result)

