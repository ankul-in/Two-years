#kata
#https://www.codewars.com/kata/552e45cc30b0dbd01100001a/train/python

def zipvalidate(code):
    if len(code) != 6:
        return False
    if not code.isdigit():
        return False
    if code[0] in {'0', '5', '7', '8', '9'}:
        return False
    return True

