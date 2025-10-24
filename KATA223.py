#kata
#https://www.codewars.com/kata/56a127b14d9687bba200004d/train/python

#well i remember this 
import math
def number_of_routes(m: int, n: int) -> int:
    return math.comb((m+n),n)

print(number_of_routes(100,3))