#linear search
a=[]
flag=0
n=int(input("enter number of items-->"))
for i in range(n):
    x=int(input("enter the number-->"))
    a.append(x)
x=int(input("enter number to search in array-->"))
for i in range(1,len(a)):
    if x==a[i]:
        print("number found at this index-->",i)
        flag=1
if flag == 0:
    print("number not found in list!!! wanna add it")