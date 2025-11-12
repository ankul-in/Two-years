#kata
#https://www.codewars.com/kata/52705ed65de62b733f000064/train/python


def sort_list(sort_by, lst):
    return sorted(lst, key=lambda x: x[sort_by], reverse=True)