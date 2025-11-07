#kata
#https://www.codewars.com/kata/56abc5e63c91630882000057/train/python

def next_numb(val):
    if len(str(val))>9:
        return "There is no possible number that fulfills those requirements"
    while True:
        val+=1
        if val%3==0:
            if val%2!=0:
                if len(set(str(val)))==len(list(str(val))):
                    return val
        
def next_numb(val):
    i = val + 1
    while i <= 9999999999:
        if i % 3 == 0 and i % 2 and len(str(i)) == len(set(str(i))):
            return i
        i += 1
    return 'There is no possible number that fulfills those requirements'