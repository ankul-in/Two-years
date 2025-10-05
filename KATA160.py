#kata
#

# import gmpy2 as gm

# def step(g, m, n):
#     a=m
#     b=m
#     while a>=m and a<n:
#         x=gm.is_prime(a)
#         if x:
#             while b>m and b<n:
#                 y=gm.is_prime(b)
#                 if y:
#                     if b-a==g:
#                         return [a,b]
#                     b=gm.next_prime(b)
#         a=gm.next_prime(a)
#     return []

import gmpy2 as gm

def step(g, m, n):
    a = gm.next_prime(m - 1)
    while a < n:
        b = a + g
        if b < n and gm.is_prime(b):
            return [a, b]
        a = gm.next_prime(a)
    return []
print(step(6,1,100))

#damn solution
from gmpy2 import is_prime
def step(g, m, n):
    for i in range(m, n-g+1):
        if is_prime(i) and is_prime(i+g):
            return [i, i+g]