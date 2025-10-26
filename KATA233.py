#kata
#https://www.codewars.com/kata/551186edce486caa61000f5c/train/python
#hell yeah fynmann 
def count_squares(n):
    x=0
    for i in range(n):
        x+=(i+1)*(i+1)
    return x
print(count_squares(20))