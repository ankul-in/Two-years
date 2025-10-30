#kata
#https://www.codewars.com/kata/5a005f4fba2a14897f000086/train/python

def sum_it_up(arr):
    total=0
    for num,base in arr:
        total+=int(num,base)
    return total

            