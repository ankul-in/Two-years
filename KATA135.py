#kata
#https://www.codewars.com/kata/580a0347430590220e000091/train/python
def area(d, l): 
    if d<=l:
        return "Not a rectangle"
    return round(((d**2-l**2)**0.5)*l,2)