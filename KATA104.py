#kata
#https://www.codewars.com/kata/590938089ff3d186cb00004c/train/python


# from itertools import combinations , combinations_with_replacement , permutations ,accumulate


# a=[1, 2, 3]
# perm=permutations(a)
# comb=combinations(a,3)
# combR=combinations_with_replacement(a,3)
# print(list(perm),list(comb),list(combR))
# acc=accumulate(a[::-1])
# print(list(acc))

from itertools import accumulate
def suffix_sums(arr):
    return list(accumulate(arr[::-1]))[::-1]