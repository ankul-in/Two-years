#kata
#https://www.codewars.com/kata/65cf8417e2b49c2ecd3c3aee/train/python

def zeros(n: int) -> int:
    if n == 1:
        return 2  
    a, b = 2, 1  
    for _ in range(3, n + 1):
        a, b = a + b, a
    return a

print(zeros(6754))

#damn
from gmpy2 import fib
zeros = lambda n: 2 if n==1 else fib(n+1)