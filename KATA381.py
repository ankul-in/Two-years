#kata
#https://www.codewars.com/kata/538948d4daea7dc4d200023f/train/python

def convert_bits(a, b):
    count=0
    x=list(bin(a)[2:])
    y=list(bin(b)[2:])
    max_len = max(len(x), len(y))
    m = ["0"] * (max_len - len(x)) + x
    n = ["0"] * (max_len - len(y)) + y
    for i,j in zip(m,n):
        if i!=j:
            count+=1
    return count