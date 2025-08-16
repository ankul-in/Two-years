#diffie hellman algorithm
def power(a,b,p):
    if b==1:
        return a 
    else:
        return pow(a,b)%p
def main():
    P=23
    print("the value of p is -->",P)
    G=9
    print("the value of g is -->",G)
    a=4
    print("the private key for a is -->",a)
    x=pow(G,a,P)
    b=3
    print("the private key for b is -->",b)
    y=power(G,b,P)
    ka=power(y,a,P)
    kb=power(x,b,P)
    print("secret key for a -->",ka)
    print("secret key for b is -->",kb)
if __name__ =="__main__":
    main()