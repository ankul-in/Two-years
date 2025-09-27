#kata
#https://www.codewars.com/kata/61fef3a2d8fa98021d38c4e5/train/python
#this one times out
# def card_game(n):
#     alice,bob=0,0
#     while n>0:
#         if n%2==0:
#             alice+=n/2
#             n=n/2
#             bob+=1
#             n=n-1
#         else:
#             alice+=1
#             n=n-1
#             bob+=1
#             n=n-1
#         print(n)
#     return alice

#using dfs

def card_game(n):
    from functools import lru_cache

    @lru_cache(None)
    def dfs(turn , cards):
        if cards == 0:
            return 0
        if cards % 2 == 1:
            taken = 1
            if turn ==0:
                return taken+dfs(1,cards-taken)
            else:
                return dfs(0,cards-taken)
        else:
            taken_one=1+dfs(1-turn,cards -1) if turn == 0 else dfs(1-turn,cards-1)
            taken_half = (cards//2+dfs(1-turn,cards //2)) if turn ==0 else dfs(1-turn,cards//2)
            return max(taken_one,taken_half) if turn == 0 else min(taken_one,taken_half)
    return dfs(0,n)


print(card_game(10))
