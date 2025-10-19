#kata
#https://www.codewars.com/kata/6411b91a5e71b915d237332d/train/python

def valid_parentheses(paren_str):
    count=0
    for i in paren_str:
        if count<0:
            return False
        if i=="(":
            count+=1
        if i==")":
            count-=1
    return count==0


################################
def valid_parentheses(x):
    while "()" in x:
        x = x.replace("()", "")
    return x == ""