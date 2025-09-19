#kata
#https://www.codewars.com/kata/54e9554c92ad5650fe00022b/train/python
def to_currency(price):
    answer=[]
    x=""
    reverse=str(price)[::-1]
    for i,j in enumerate(reverse):
        x+=j
        if (1+i) % 3 == 0:
            answer.append(x[::-1])
            x=""
    if x:
        answer.append(x[::-1])
    return ",".join(answer[::-1])

def to_currency(price):
    return f"{price:,}"