#check if number is palindrome
num=int(input("enter a number-->"))
temp = num
rev=0
while (num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if (temp==rev):
    print("number is palindrome")
else :
    print("number is not a palindrome")
