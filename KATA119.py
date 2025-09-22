#kata
#https://www.codewars.com/kata/58daa7617332e59593000006/train/python
def find_longest(arr):
    long=""
    for i in arr:
        if len(str(i))>len(long):
            long=str(i)
    return int(long)
print(find_longest([1, 200, 100000]))

#use max function next time
def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))

