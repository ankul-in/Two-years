#kata
#https://www.codewars.com/kata/587a88a208236efe8500008b/train/python

def sequence_sum(b, e, s):
    if s==0 or (s>0 and b>e) or (s<0 and b<e):
        return 0
    terms = ((e-b)//s)+1
    return (terms*(b+(b+(terms-1)*s)))//2

#so neat
def sequence_sum(a, b, step):
    n = (b-a)//step
    return 0 if n<0 else (n+1)*(n*step+a+a)//2