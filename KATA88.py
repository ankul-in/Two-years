#kata
#https://www.codewars.com/kata/59f3178e3640cef6d90000d5/train/python


from itertools import combinations_with_replacement
def find(arr,n):
    counter=0
    comb=[]
    for i in range(len(arr)+1):
        comb+=combinations_with_replacement(arr,i)
    for i in comb:
        if sum(i)==n:
            counter+=1
    return counter
find([3,6,9,12],12)