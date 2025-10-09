#kata
#https://www.codewars.com/kata/57470efebf81fea166001627/train/python
def letter_check(arr): 
    a=set((arr[1]).lower())
    b=set((arr[0]).lower())
    return a.issubset(b)
print(letter_check(["abcd", "aaa"]))
