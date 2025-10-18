#kata
#https://www.codewars.com/kata/581331293788bc1702001fa6/train/python


def mirror(text):
    answer=[]
    length=0
    x=text.split()
    
    for i in x:
        answer.append("* "+i[::-1])
        length=max(len(i),length)
    strin="*"*(length+4)+"\n"
    for i in answer:
        i=i.ljust(length+2)+" *"
        strin=strin+i+"\n"
    return strin+"*"*(length+4)
print(mirror("emosewA !ataK"))

"""
***********
* Awesome *
* Kata!   *
***********
"""
