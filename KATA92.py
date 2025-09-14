#kata
#https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python


def remove_every_other(my_list):
    answer=[]
    for i in range(len(my_list)):
        if i%2==0:
            answer.append(my_list[i])
    return answer

#yeah i feel dumb after this solution
def remove_every_other(my_list):
    return my_list[::2]