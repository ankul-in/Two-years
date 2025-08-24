#https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1&selectedLang=python3
#maximum recursion depth = 991

def printN(n,current=1):
    if current>n:
        return
    else:
        print(current,end=" ")
        current+=1
        printN(n,current)

n=int(input("enter numbers to print via recursion-->"))
printN(n)