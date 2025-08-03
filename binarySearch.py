def binSearch(A,a,b,q):
    m=int((a+b)/2)
    if(q<A[m]):
        binSearch(A,a,m,q)
    elif(q>A[m]):
        binSearch(A,m,b,q)
    elif(q==A[m]):
        print("Number found at index -->")
        print(m)
    else:
        print("Number not available in list")

A=[]
x=int(input("enter number of units you want to enter-->"))
for i in range(x):
    y=int(input("enter number-->"))
    A.append(y)

q=int(input("enter the number you want to index-->"))
a=A[0]
b=A[-1]
binSearch(A,a,b,q)