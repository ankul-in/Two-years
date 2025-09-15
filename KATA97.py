#kata
#https://www.codewars.com/kata/560b8d7106ede725dd0000e2/train/python


from gmpy2 import is_prime as ip

def prime_bef_aft(num):
    for k in range(num-1,1,-1):
        if ip(k):
            before=k
            break
    for k in range(num+1,200000):
        if ip(k):
            after=k
            break
    return [before,after]

print(prime_bef_aft(100))



# #def prime(a):
#     if a < 2: return False
#     if a == 2 or a == 3: return True   
#     if a % 2 == 0 or a % 3 == 0: return False
#     maxDivisor = a**0.5
#     d, i = 5, 2
#     while d <= maxDivisor:
#         if a % d == 0: return False
#         d += i 
#         i = 6 - i
 
#     return True

# def prime_bef_aft(num):
#     res = []
#     for n in range(num-1, 1, -1):
#         if prime(n):
#             res.append(n)
#             break
#     for n in range(num+1, 3*num, 1):
#         if prime(n):
#             res.append(n)
#             break
#     return res