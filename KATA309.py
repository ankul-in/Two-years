#kata
#https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python

def divisors(n):
    result = [i for i in range(2, n) if n % i == 0]
    return result if result else f"{n} is prime"

