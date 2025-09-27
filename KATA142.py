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

#using dfs maximum depth reached f
# def card_game(n):
#     from functools import lru_cache

#     @lru_cache(None)
#     def dfs(turn , cards):
#         if cards == 0:
#             return 0
#         if cards % 2 == 1:
#             taken = 1
#             if turn ==0:
#                 return taken+dfs(1,cards-taken)
#             else:
#                 return dfs(0,cards-taken)
#         else:
#             taken_one=1+dfs(1-turn,cards -1) if turn == 0 else dfs(1-turn,cards-1)
#             taken_half = (cards//2+dfs(1-turn,cards //2)) if turn ==0 else dfs(1-turn,cards//2)
#             return max(taken_one,taken_half) if turn == 0 else min(taken_one,taken_half)
#     return dfs(0,n)

#and this too is wrong
def card_game(n):
    alice=0
    turn=0
    while n>0:
        if n%2 == 1:
            n-=1
            if turn ==0:
                alice+=1
        else:
            half = n//2
            if half %2 ==1 or half == 2:
                n-=1
                if turn == 0:
                    alice +=1
            else:
                n=half
                if turn == 0 :
                    alice +=half
        turn ^= 1
    return alice +1 

print(card_game(12))
