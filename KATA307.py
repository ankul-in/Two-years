#kata
#https://www.codewars.com/kata/588854201361435f5e0000bd/train/python

def array_conversion(arr):
    iteration = 1
    while len(arr) > 1:
        new_arr = []
        for i in range(0, len(arr), 2):
            if iteration % 2 == 1:  
                new_arr.append(arr[i] + arr[i+1])
            else:  
                new_arr.append(arr[i] * arr[i+1])
        arr = new_arr
        iteration += 1
    return arr[0]

