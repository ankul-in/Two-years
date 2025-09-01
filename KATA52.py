#https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
#kata


def xo(s):
    counter=0
    for i in list(s):
        
        if i.lower()=="x":
            counter+=1
        elif i.lower()=="o":
            counter-=1
    if counter==0:
        return True
    return False
        