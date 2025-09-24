#kata
#https://www.codewars.com/kata/68c7c3cb12252d313dc9fd8b/train/python
def is_palindrome(n: int) -> bool:
    n=bin(n)[2:]
    return str(n) == str(n)[::-1] 