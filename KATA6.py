#outputs sum of rows , of triangle formed using odd integers
def row_sum_odd_numbers(n):
    # for i in range(n):
    #     if i%2!=0:
    #         arr=[]
    #         arr.append(i)
    # for j in range(n):
    #     for k in range(j):
    #         arr1=[]
    #         arr1.append(arr.pop(k)) 
    # initialization number of row n
    initial=(n*(n-1))+1
    sum=0
    for i in range(2*n):
        if i%2==0:
            sum=sum+(initial+i)
    return sum
#yeah i did that ngl
