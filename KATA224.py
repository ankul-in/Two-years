#kata
#https://www.codewars.com/kata/531963f82dde6fc8c800048a/train/python

def solved(s): 
    mid = len(s) // 2
    if len(s)%2!=0:
        s = s[:mid] + s[mid+1:]  
    return "".join(sorted(s))