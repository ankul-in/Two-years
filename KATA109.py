#kata
#https://www.codewars.com/kata/5516ab668915478845000780/train/python
def reverse_by_center(s):
    length=len(s)
    if length % 2 == 0:
        return s[(length//2):]+s[:(length//2)]
    else:
        return s[(length//2)+1:]+s[(length//2)]+s[:(length//2)]