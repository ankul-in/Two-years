#kata
#https://www.codewars.com/kata/57882daf90b2f375280000ad/train/python
def sumsquares(lst):
    sum=0
    
    for i in lst:
        if (isinstance(i, list)) :
            sum+=sumsquares(i)
        try:
            sum+=i*i
        except:
            pass
    return sum

print(sumsquares([1,[[3],10,5,[2,[3],[4],[5,[6]]]]]))


def sumsquares(l):
    return sum([ i**2 if type(i) == int else sumsquares(i) for i in l ])
#could have thought like that 