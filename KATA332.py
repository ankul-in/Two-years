#kata
#https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/python

def seven(m):
    steps = 0
    while m > 99:  
        x, y = divmod(m, 10)   
        m = x - 2 * y          
        steps += 1
    return (m, steps)

