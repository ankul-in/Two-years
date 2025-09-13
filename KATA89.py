#kata
#https://www.codewars.com/kata/56b18992240660a97c00000a/train/python

from itertools import permutations
def permutation_average(n):
    m=list(str(n))
    perm=set(permutations(m))
    print(list(perm))
    perm_values = [int(''.join(p)) for p in perm]
    return round(sum(perm_values)/len(perm_values))

print(permutation_average(25))