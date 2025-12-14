#kata
#https://www.codewars.com/kata/56ee0448588cbb60740013b9/train/python

def mystery(n):
    if n <= 0:
        return []
    return [d for d in range(1, n+1) if n % d == 0 and d % 2 == 1]

