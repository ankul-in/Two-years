#kata
#https://www.codewars.com/kata/5609fd5b44e602b2ff00003a/train/python

def process_2arrays(arr1, arr2):
    set1,set2=set(arr1),set(arr2)
    a=len(set1 & set2)
    b=len(set1 ^ set2)
    c=len(set1 - set2)
    d=len(set2 - set1)
    
    return[a, b, c, d]

print(process_2arrays([1, 2 ,3,4, 5 ,6 ,7 ,8 ,9],[2, 4, 6, 8, 10, 12, 14]))