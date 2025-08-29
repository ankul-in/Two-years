#kata
#https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
    if not text:
        return text

    import re
    words = re.split('[-_]', text)
    first = words[0]
    rest = [w.capitalize() for w in words[1:]]

    return first + ''.join(rest)