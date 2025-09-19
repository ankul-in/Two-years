#kata
#https://www.codewars.com/kata/56069d0c4af7f633910000d3/train/python

def search(budget, prices):
    answer=[]
    for i in prices:
        if i <= budget:
            answer.append(i)
            answer=sorted(answer)
    return ",".join([str(i) for i in answer])


#why didnt i think of this
"""def search(budget, prices):
    return ','.join(str(a) for a in sorted(prices) if a <= budget)"""