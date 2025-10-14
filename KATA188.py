#kata
#https://www.codewars.com/kata/5a0366f12b651dbfa300000c/train/python

def arbitrate(inp, n):
    for j,i in enumerate(inp):
        if i=="1":
            return inp[:j+1]+"0"*(len(inp)-j-1)
    return inp
print(arbitrate("00010000001001010011",6))


#why didnt i thought of this
def arbitrate(s, n):
    i = s.find('1') + 1
    return s[:i] + '0' * (n - i)