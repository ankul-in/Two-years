#12 area of triangle with 3 given sides
a=float(input("enter first side length-->"))
b=float(input("enter second side length-->"))
c=float(input("enter third side length-->"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c) )**0.5
print(area,"unit sq")