#compound interest
p=int(input("enter principle amount-->"))
r=int(input("enter rate-->"))
t=int(input("enter time-->"))

for i in range(t):
    p=p+ (p*r/100)

print("total value",p)