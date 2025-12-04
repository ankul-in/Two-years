#kata
#https://www.codewars.com/kata/58a3c1f12f949e21b300005c/train/python

def lamps(a):
    n = len(a)
    alt0 = [i % 2 for i in range(n)]
    alt1 = [(i + 1) % 2 for i in range(n)]
    cost0 = sum(a[i] != alt0[i] for i in range(n))
    cost1 = sum(a[i] != alt1[i] for i in range(n))
    
    return min(cost0, cost1)

