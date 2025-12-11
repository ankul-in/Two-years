#kata
#https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))




def descending_order(num):
    return int("".join(map(str,sorted([int(i) for i in str(num)],reverse=True))))