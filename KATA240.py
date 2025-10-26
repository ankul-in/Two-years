#kata240
#https://www.codewars.com/kata/570fd7ad34e6130455001835/train/python

def zebulans_nightmare(function):
    x=function.split("_")
    answer=[x[0]]
    for i in x[1:]:
        answer.append(i.capitalize())
    return "".join(answer)   


def zebulans_nightmare(function):
    answer=[]
    x=function.split("_")
    for i in range(len(x)):
        if i == 0:
            answer.append(x[i])
        else:
            answer.append(x[i].capitalize())
    return "".join(answer) 


print(zebulans_nightmare('convert_to_uppercase'))