#kata
#https://www.codewars.com/kata/58e67378fd2d897b8a000110/train/python

def num_combo(xs: list, n: int):
    total_sum = sum(xs)
    count = 0
    for i in range(len(xs)):
        if total_sum - xs[i] == n:
            count += 1
    return count

