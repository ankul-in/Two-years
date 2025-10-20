#kata
#https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    positive,negative=0,0
    for i in arr:
        if i>0:
            positive+=1
        elif i<0:
            negative+=i
        else:
            pass
    return [positive,negative]