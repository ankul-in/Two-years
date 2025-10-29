#kata
#https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python

def multi_table(number):
    str=""
    for i in range(1,11):
        str+=f"{i} * {number} = {number*i}\n"
    return str[:-1]