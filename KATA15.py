# #product of consecutive fibonacci sequence
# def fibonacci(n):
#     a=0
#     b=1
#     arr=[0,1]
#     for i in range(n):
#         c=a+b
#         arr.append(c)
#         a=b
#         b=c
#     return arr
# x=fibonacci(30)
# prod=[]
# for i in range(len(x)-1):
#    prod.append(x[i] * x[i+1])

# def checkProd(num):
#     for i in prod:
#         if i==num:
#             return True
#         else:
#             return False

def product_fib(_prod):
    a, b = 0, 1
    while a * b < _prod:
        a, b = b, a + b
    if a * b == _prod:
        return [a, b, True]
    else:
        return [a, b, False]