#kata
#https://www.codewars.com/kata/55a7de09273f6652b200002e/train/python


# def lucasnum(n):
#     if not isinstance(n, int):
#         raise ValueError("Input must be an integer.")
    
#     if n == 0:
#         return 2
#     elif n == 1:
#         return 1
#     elif n > 1:
#         a, b = 2, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return a
#     else:  # n < 0
#         a, b = 2, 1
#         for _ in range(-n):
#             a, b = b, b - a
#         return a

def lucasnum(n):
    a, b = 2, 1
    k = abs(n)
    for _ in range(k):
        a, b = b, a + b
    if n >= 0:
        return a
    else:
        return ((-1) ** k) * a
print(lucasnum(-1))