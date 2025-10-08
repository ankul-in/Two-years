#kata
#https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3/train/python

def calculate(strng):
    x=strng.split()
    if x[-2]=="gains":
        return int(x[2])+int(x[-1])
    elif x[-2]=="loses":
        return int(x[2])-int(x[-1])

def calculate(s):
    x=[int(i) for i in s.split() if i.isdigit()]
    return sum(x) if 'gains' in s.split() else x[0]-x[1]


print(calculate("Tom has 20 apples and gains 15"))
