#it counts number of 1s in your binary of decimal input

def count_bits(n):
    
    x=bin(n)[2:]
    y=0
    z=list(x)
    for i in z:
        if i=="1":
            y+=1
    print(x)           
    return y
count_bits(678)

print(count_bits(678))