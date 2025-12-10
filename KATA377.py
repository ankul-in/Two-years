#kata
#https://www.codewars.com/kata/559d7951ce5e0da654000073/train/python

def alternate_sq_sum(arr):
    answer=[]
    for i,j in enumerate(arr):
        if i%2!=0:
            answer.append(j**2)
        else:
            answer.append(j)
    return sum(answer)