#kata
#https://www.codewars.com/kata/593f50f343030bd35e0000c6/train/python

def encode(s):
    answer=""
    for i in s:
        if i.isalpha():
            if ord(i)%2!=0:
                answer+="0"
            else:
                answer+="1"
        else:
            answer+=i
    return answer
