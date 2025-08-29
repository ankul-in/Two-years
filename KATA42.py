#https://www.codewars.com/kata/58bccdf56f25ff6b6d00002f

#kata

def rounding(n, m):
    lower = (n // m) * m
    upper = lower + m
    diff_lower = n - lower
    diff_upper = upper - n

    if diff_lower == diff_upper:
        return n
    return lower if diff_lower < diff_upper else upper