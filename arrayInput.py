def arrayInput():
    arr=[]
    n=int(input("enter number of digits in array"))
    for i in range(n):
        x=int(input("enter digit-->"))
        arr.append(x)
    return arr