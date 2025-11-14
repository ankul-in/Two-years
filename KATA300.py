#kata
#https://www.codewars.com/kata/56b97b776ffcea598a0006f2/train/python

def bubblesort_once(k):
    l=k[:]
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            l[i],l[i-1]=l[i-1],l[i]
    return l
            