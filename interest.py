#simple interest 18
p=float(input("enter principle amount-->"))
r=float(input("enter rate of interest-->"))
t=float(input("enter time-->"))
simpleInterest = (p*r*t)/100
total = simpleInterest + p
print("total amount to be extracted-->",total)


n=float(input("enter number of times per year your amount compounds-->"))
compoundInterest = p * ((1 + (r / n)) ** (n * t))

total=compoundInterest+p
print("total amout to be extracted",total)
