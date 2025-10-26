#kata
#https://www.codewars.com/kata/5a3f2925b6cfd78fb0000040/train/python

def solve(st):
    if len(st)%2 != 0:
        return -1
    openp=0
    closep=0
    for i in st:
        if i == "(":
            openp+=1
        elif i==")":
            if openp>0:
                openp-=1
            else:
                closep+=1
    return (openp + closep) // 2 + (openp % 2)