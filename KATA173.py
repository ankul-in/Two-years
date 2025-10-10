#kata
#https://www.codewars.com/kata/6863033d9c452af74e0983b7/train/python

def socks(colours, pairs):
    return 2 * pairs + (colours - 1)

print(socks(7, 4))
#damn solution
socks=lambda O,o:o+~-O+o