#kata
#https://www.codewars.com/kata/5b1d1812b6989d61bd00004f/train/python

def find_nth_occurrence( substring,string, n):
    start = 0
    count = 0
    
    while True:
        index = string.find(substring, start)
        if index == -1:  # no more occurrences
            return -1
        count += 1
        if count == n:
            return index
        start = index + 1

