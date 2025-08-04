#program to find armstrong number 

num=int(input("enter the number to check if its armstrong-->"))
temp=num
len=len(str(num))
arms=0
for i in range(len):
    remainder=num%10
    num=num//10
    arms=arms+(remainder**len)
if arms==temp:
    print("number is armstrong")
else:
    print("number is Not armstrong")
