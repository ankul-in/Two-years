#kata
#https://www.codewars.com/kata/552ab0a4db0236ff1a00017a/train/python

def sillycase(silly):
    max=-(-len(silly)//2) #-(-a // b)

    first=silly[:max].lower()
    second=silly[max:].upper()
    return first+second