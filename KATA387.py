#kata
#https://www.codewars.com/kata/546e2562b03326a88e000020/

def square_digits(num):
    answer=[]
    for j in [int(i) for i in str(num)]:
        answer.append(str(j**2))
    return int("".join(answer))