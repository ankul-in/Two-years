#kata
#https://www.codewars.com/kata/6914c975e159c8f7e120cc84/train/python

def find_lineup(memories):
    n = len(memories)
    order = [None] * n
    for i, m in enumerate(memories, start=1):  
        pos = m + 1
        if pos > n or order[pos-1] is not None:
            return []  
        order[pos-1] = i
    
    return order