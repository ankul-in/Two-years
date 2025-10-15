#kata
#https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python

def jumping_number(number):
    x=[int(i) for i in str(number)]
    diff= [j - i for i, j in zip(x, x[1:])]
    if all(diff[i] == 1 or diff[i]== -1 for i in range(len(diff))): 
        return "Jumping!!"
    else:
        return "Not!!"
    

print(jumping_number(98789876))