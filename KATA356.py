#kata
#https://www.codewars.com/kata/56fe97b3cc08ca00e4000dc9/train/python

def sc(apple):
    for i,j in enumerate(apple):
        for k,l in enumerate(j):
            if l=="B":
                return (i,k)
    return None