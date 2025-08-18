n=5

a, b = 0, 1
sum=0
x=0
while x<n:
        sum+=a
        a, b = b, a + b
        x+=1

print(sum)