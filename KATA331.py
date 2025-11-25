#kata
#https://www.codewars.com/kata/593c9175933500f33400003e/solutions/python

def multiples(m, n):
    answer=[]
    for i in range(1,m+1):
        answer.append(n*i)
    return answer