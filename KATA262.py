#kata
#https://www.codewars.com/kata/51f082ba7297b8f07f000001/train/python
def find_in_array(seq, func): 
    for index, value in enumerate(seq):
        if func(value, index):
            return index
    return -1

print(find_in_array([1,3,5,6,7], lambda v, i: v % 2 == 0))