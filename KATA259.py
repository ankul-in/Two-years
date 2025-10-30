#kata
#https://www.codewars.com/kata/5464cbfb1e0c08e9b3000b3e/train/python

def is_happy(n):
    sumSet=set()
    while  n!=0 and n not in sumSet:
        sumSet.add(n)
        n=sum(int(digit)**2 for digit in str(n))
    return n==1
    
    