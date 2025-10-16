#kata
#https://www.codewars.com/kata/52b305bec65ea40fe90007a7/train/python

def grabscrab(said, possible_words):
    answer=[]
    for i in possible_words:
        if sorted(list(i))==sorted(list(said)):
            answer.append(i)
    return answer