import random
print(random.random())
n=int(input("enter number of digits you want-->"))
x=int((n/10)+1)
y=int((10**n))
print(random.randint(x,y))