#kata https://www.codewars.com/kata/58f174ed7e9b1f32b40000ec/train/python
from itertools import combinations

def max_profit(prices):
    profit=float('-inf')
    comb = combinations(prices,2)
    for a,b in comb:
        diff=b-a
        if diff > profit:
            profit=diff
    return profit

    

max_profit([10, 7, 5, 4, 1])