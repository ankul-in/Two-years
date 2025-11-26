#kata
#https://www.codewars.com/kata/580777ee2e14accd9f000165/train/python

def skiponacci(n):
    answer=[]
    a,b=1,1
    for i in range(n):
        if i%2==0:
            answer.append(str(a))
        else:
            answer.append("skip")
        a,b=b,a+b
    return " ".join(answer)