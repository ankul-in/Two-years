#kata
#https://www.codewars.com/kata/5813d19765d81c592200001a/train/python

def dont_give_me_five(start,end):
    answer=[]
    for i in range(start,end+1):
        if "5" in str(i):
            continue
        else:
            answer.append(i)
    return len(answer)