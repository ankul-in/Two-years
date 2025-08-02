num=int(input("enter number to check if its prime or not -->"))
flag=0
for i in range (2,int(num/2)):
    if num%i==0:
        flag=flag+1
    
if flag>0:
    print("number is NOT prime")
else:
    print("number is a prime")

