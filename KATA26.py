#kata https://www.codewars.com/kata/588e27b7d1140d31cb000060/train/python
#generate pairs in increasing order
def generate_pairs(n):
    arr=[]
    for i in range(n+1):
        for j in range(i,n+1):
            arr.append([i,j])
    return arr