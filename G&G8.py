#https://www.geeksforgeeks.org/problems/juggler-sequence3930/1&selectedLang=python3
import math
def juggleNum(n):
    print(n,end=" ")
    if n==1:
        return
    if n%2==0:
        n=math.floor(math.sqrt(n))
        print("is even then",n,end="\n")
    else:
        n=math.floor(math.sqrt(math.pow(n,3)))
        print("is odd then",n,end="\n")
    juggleNum(n)
    


n=int(input("enter number to start juggle-->"))
juggleNum(n)
