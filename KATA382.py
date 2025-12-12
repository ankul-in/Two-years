#kata
#https://www.codewars.com/kata/5714803d2817ffce17000a35/train/python


def find_a_b(numbers, c):
    n = len(numbers)
    for i in range(n):
        a = numbers[i]
        for j in range(i+1, n):
            b = numbers[j]
            if a * b == c:
                return [a, b]
    return None