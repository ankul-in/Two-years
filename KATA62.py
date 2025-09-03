#kata
#https://www.codewars.com/kata/58f8b35fda19c0c79400020f/train/python


def all_non_consecutive(arr):
    result=[]
    prev=arr[0]-1
    for i,j in enumerate(arr):
        if j-1!=prev:
            x={}
            x['i']=i
            x['n']=j
            result.append(x)
        prev=j
    return result