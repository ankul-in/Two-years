#kata
#https://www.codewars.com/kata/5416f1834c24604c46000696/train/python

def cycle(sequence):
    seen={}
    for i,val in enumerate(sequence):
        if val in seen:
            mu=seen[val]
            lam=i-mu
            return [mu,lam]
        seen[val]=i
    return []

print(cycle([1,2,3,4,2,3,4]))