#def solve(a,b):
#kata
#https://www.codewars.com/kata/59aa6567485a4d03ff0000ca/train/python
import gmpy2
def list_prime(a,b):
    primelist=[]
    for num in range(a,b):
        if gmpy2.is_prime(num):
            primelist.append(num)
    return primelist
def happy_number(prime):
    lister=[]
    while True:
        sum_of_squares = sum(int(digit)**2 for digit in str(prime))
        if sum_of_squares == 1:
            counter = 1
            return True
        if sum_of_squares in lister:
            return False
        lister.append(sum_of_squares)
        prime = sum_of_squares
        #return True
def solve(a,b):
    prime = list_prime(a,b)
    lister = []
    counter = 0
    returncounter=0
    answer=[]
    for i in list_prime(a,b):
        answer.append(happy_number(i))
    counter=0
    for i in answer:
        if i == True:
            counter+=1
    return counter

print(solve(0,1000))


