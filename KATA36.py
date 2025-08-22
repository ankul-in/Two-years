#kata https://www.codewars.com/kata/55983863da40caa2c900004e/train/python


from itertools import permutations

def next_bigger(n):
    digits = list(str(n))
    perms = sorted(set(int(''.join(p)) for p in permutations(digits)))
    for num in perms:
        if num > n:
            return num
    return -1