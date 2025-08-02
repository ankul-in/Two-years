n=int(input("enter the digits of fibonacci series you want -->" ))
l=[]
a=0
b=1
l.append(a)
l.append(b)

for i in range (1,n-1):
    c=a+b
    l.append(c)
    a=b
    b=c
print(l)