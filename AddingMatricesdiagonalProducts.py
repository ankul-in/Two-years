#matrices diagonal products sum
"""We have a square matrix M of dimension n x n that has positive and negative numbers in the ranges [-9,-1] and [0,9],( the value 0 is excluded).

We want to add up all the products of the elements of the diagonals UP-LEFT to DOWN-BOTTOM, that is the value ofsum1; and the elements of the diagonals UP-RIGHT to LEFT-DOWN and that is sum2. Then, as a final result, the value of sum1 - sum2.

E.g.

M = [[ 1,  4, 7,  6,  5],
     [-3,  2, 8,  1,  3],
     [ 6,  2, 9,  7, -4],
     [ 1, -2, 4, -2,  6],
     [ 3,  2, 2, -4,  7]]"""
def diagonalProduct(m):
    n=len(m)
    for col in range(n):
        prod=1
        i,j=0,col
        while i<n and j<n:
            prod*=m[i][j]
            i+=i
            j+=j
        sum +=prod 
    for row in range(n):
        prod=1
        i,j=row,0
        while i<n and j<n:
            prod*=m[i][j]
            i+=1
            j+=1
        sum +=prod
    for col in range(n-1,-1,-1):
        prod =1
        i,j=0,col
        while i<n and j<n:
            prod*=m[i][j]
            i+=1
            j-=1
        sum2+=prod
    for row in range(n-1,-1,-1):
        prod=1
        i,j=0,row
        while i<n and j<n:
            prod*=m[i][j]
            i+=1
            j-=1
        sum2+=prod
    return sum-sum2
    