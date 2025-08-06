#hcf
def hcf(a,b):
    if a>b:
        x=b
    elif b>a:
        x=a
    else:
        print("hcf-->",a)
    for i in range(1,x+1):
        if a%i==0 and b%i==0:
            hcf=i
    print("hcf-->",hcf)
print("program to find hcf")
a=int(input("enter first number-->"))
b=int(input("enter second number-->"))
hcf(a,b)