#kata https://www.codewars.com/kata/58f174ed7e9b1f32b40000ec/train/python
# from itertools import combinations

# def max_profit(prices):
#     profit=float('-inf')
#     comb = combinations(prices,2)
#     for a,b in comb:
#         diff=b-a
#         if diff > profit:
#             profit=diff
#     return profit
def max_profit(prices: list[int]) -> int:
    min_price = 10**10  # "infinity"
    max_profit = -10**10
    for p in prices:
        max_profit = max(max_profit, p - min_price)
        min_price = min(min_price, p)
    return max_profit