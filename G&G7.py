#https://www.geeksforgeeks.org/problems/fibonacci-series-up-to-nth-term/1&selectedLang=python3
def printfib(n):
    a=0
    b=1
    x=0
    while x<n:
        a,b=b,a+b
        print(a,end=" ")
        x+=1
        
n=int(input("enter number of terms of fib-->"))
printfib(n)