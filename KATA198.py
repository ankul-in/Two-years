#kata
#https://www.codewars.com/kata/5a1ebc2480171f29cf0000e5/solutions/python

def sort_by_area(seq): 
    answer=[]
    for i in seq:
        if isinstance(i,tuple):
            answer.append(i[0]*i[1])
        elif isinstance(i,float) or isinstance(i,int):
            answer.append(3.14*(i**2))

    print(answer)
    x=zip(seq,answer)
    y=sorted(x, key=lambda x: x[1])
    print(y)
    return [i for i,j in y]

print(sort_by_area([ (2, 5), 6 ]))



###################
def sort_by_area(seq): 
    def func(x):
        if isinstance(x, tuple):
            return x[0] * x[1]
        else:
            return 3.14 * x * x
    return sorted(seq, key=func)