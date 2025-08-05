#biggest out of 3
a=int(input("enter 1st number -->"))
b=int(input("enter 2nd number -->"))
c=int(input("enter 3rd number -->"))
if a>b :
    if a>c :
        print("1st number is biggest",a)
    else:
        print("3rd number is biggest",c)
else:
    if b>c:
        print("2nd number is biggest",b)
    else:
        print("3rd number is biggest",c)