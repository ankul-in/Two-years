#kata
#https://www.codewars.com/kata/54bd06539f075cece0000feb/train/python
def tick_toward(start, target):
    i=start[0]
    j=start[1]
    k=target[0]
    l=target[1]
    points=[]
    points.append((i,j))
    while (i,j) != target:
        if i<k:
            i+=1
        if j<l:
            j+=1
        if i>k:
            i-=1
        if j>l:
            j-=1
        points.append((i,j))
    return points


print(tick_toward((5,5), (5,7)))