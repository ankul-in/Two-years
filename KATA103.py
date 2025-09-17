#kata
#https://www.codewars.com/kata/54557d61126a00423b000a45/train/python


def shorter_reverse_longer(a,b):
    if len(a)<len(b):
        shorter,longer=a,b
    else:
        shorter,longer=b,a
    return shorter+longer[::-1]+shorter
print(shorter_reverse_longer("first", "abcde"))