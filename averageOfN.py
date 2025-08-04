#11 average of n digits 
n=int(input("enter number of units"))
sum=0
for i in range (n):
    num=int(input("enter your number-->"))
    sum=sum+num
avg=sum/n
print("average of your numbers is -->",avg)