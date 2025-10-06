#kata
#https://www.codewars.com/kata/56b7251b81290caf76000978/train/python

# def fibonacci(n):
#     a,b=0,1
#     while n!=0:
#         c=a
#         a=b
#         b=int(str(a+c)[-1:])
#         #print(a,b,end=" ")
#         n-=1
# print(fibonacci(11))

def get_last_digit(n):
    a,b=0,1
    while n!=0:
        c=a
        a=b
        b=int(str(a+c)[-1:])
        n-=1
    return a 

def get_last_digit(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 10
        print(a,b,end=" ")
    return a

print(get_last_digit(11))