    
#kata
#https://www.codewars.com/kata/61123a6f2446320021db987d/train/python

def prev_mult_of_three(n):
    for i in range(len(str(n))):
        if n%3==0:
            return n
        n=n//10
    return None
print(prev_mult_of_three(952406))

#nice recursion solution
def prev_mult_of_three(n):
    return prev_mult_of_three(n//10) if n%3 else n or None