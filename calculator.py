#calculator 27
def calculator(a,b,o):
    if o==1:
        print(a+b)
    if o==2:
        print(a-b)
    if o==3:
        print(a*b)
    if o==4:
        print(a/b)
    else:
        print("please enter correct operator index")
a=float(input("enter first number"))
b=float(input("enter second number"))
o=int(input("enter your operator from list 1=sum 2=subtract 3=multiply 4=divide"))
calculator(a,b,o)