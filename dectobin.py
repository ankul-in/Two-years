#decimal to binary
def dectobin(n):
    if n>1:
        dectobin(n//2)
    print(n%2,end="")

n=int(input("enter value of decimal-->"))
dectobin(n)