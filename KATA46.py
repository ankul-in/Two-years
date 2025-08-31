#kata
def reduce_fraction(fraction):
    
    
    a,b=fraction
    if a>b:
        x=b
    else:
        x=a
    i=1
    while i<=x:
        if (a%i==0 and b%i==0):
            a//=i
            b//=i 
            i=1
        i+=1
              
    return (a,b)
reduce_fraction((60,20))