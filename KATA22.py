#kata Perimeter of squares in a rectangle

def perimeter(n):
    
    a, b = 0, 1
    sum=0
    x=0
    while x<n+2:
        sum+=a
        a, b = b, a + b
        x+=1
    return sum*4