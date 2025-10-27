#kata
#https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2/train/python

# def validate(n):
#     answer=[]
#     x=[int(i) for i in list(str(n))]
#     if len(x)%2==0:
#         for i,j in enumerate(x):
#             if i%2!=0:
#                 answer.append(j*2)
#             else:
#                 answer.append(j)
#     else:
#         for i,j in enumerate(x):
#             if i%2==0:
#                 answer.append(j*2)
#             else:
#                 answer.append(j)
#     return sum([i-9 if i>9 else i for i in answer])==0


def validate(n):
    digits = [int(d) for d in str(n)]
    double = (len(digits) % 2 == 0) 
    total = 0
    for i, d in enumerate(digits):
        if (i % 2 == 0) == double:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


print(validate(2121))