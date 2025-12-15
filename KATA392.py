#kata
#https://www.codewars.com/kata/59c62f1bdcc40560a2000060/train/python

def solve(arr):
    even_count = 0
    odd_count = 0
    
    for item in arr:
        if isinstance(item, int):
            num = item
        elif isinstance(item, str) and item.isdigit():
            num = int(item)
        else:
            continue  
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count - odd_count