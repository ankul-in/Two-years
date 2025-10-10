#kata
#https://www.codewars.com/kata/68851563123e161332d2a84b/train/python

def has_loop(arr: list[int]) -> bool:
    previous=0
    for i in range(2*len(arr)+1):
        try:
            next=arr[previous]
            previous=next
        except:
            return False
    return True
        

print(has_loop([]))

#what monstrocity is this
def has_loop(arr: list[int]) -> bool:
    visited = set()
    index = 0
    while 0 <= index < len(arr):
        if index in visited:
            return True  
        visited.add(index)
        index = arr[index]
    return False 