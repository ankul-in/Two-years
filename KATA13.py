#sort zeroes and add them to end of list
def move_zeros(lst):
    rst=lst[:]
    count=0
    for i in lst:
        if i==0:
            rst.remove(i)
            count+=1
    for i in range(count):
        rst.append(0)
        
            
    return rst