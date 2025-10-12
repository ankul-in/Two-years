#kata
#https://www.codewars.com/kata/57b6f850a6fdc76523001162/train/python


def counter_effect(hit_count):
    string=[int(i) for i in list(hit_count)]
    temp=[]
    answer=[]
    for i in string:
        for j in range(i+1):
            temp.append(j)
        answer.append(temp)
        temp=[]
    return answer