#kata
#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
#     if not a:
#         return b
#     elif not b:
#         return a
    answer=[]
    for i in a:
        if i not in b:
            answer.append(i)
#     for j in b:
#         if j not in a:
#             answer.append(j)
    return answer

