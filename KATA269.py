#kata
#https://www.codewars.com/kata/525f039017c7cd0e1a000a26/train/python


def palindrome_chain_length(n):
    counter=0
    while True:
        counter+=1
        x=int(str(n)[::-1])
        n+=x
        if str(n)==str(n)[::-1]:
            return counter
        
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def palindrome_chain_length(n):
    counter = 0
    while not is_palindrome(n):
        n += int(str(n)[::-1])
        counter += 1
    return counter
            