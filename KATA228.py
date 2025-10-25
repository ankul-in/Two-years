#kata
#https://www.codewars.com/kata/559ce00b70041bc7b600013d/train/python
def finance(n):
    n=n+1
    total=0
    for j in range(n):
        # print((2*j,n-1+(j)))
        total+=sum([i for i in range(2*j,j+n)])
    return total

print(finance(3))

#so clean so elegant
def finance(n):
    return n * (n + 1) * (n + 2) / 2