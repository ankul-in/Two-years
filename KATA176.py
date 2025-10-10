#kata
#https://www.codewars.com/kata/6885f0a045008e707baa714b/train/python

def read(tape, head, moves):
    ans=""
    for i in list(moves):
        ans+=tape[head]
        if i=="<":
            head-=1
        elif i==">":
            head+=1
    return ans  