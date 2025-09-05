#kata
#https://www.codewars.com/kata/52840d2b27e9c932ff0016ae/train/python
def locate(seq: list, value) -> bool: 
    for i in seq:
        if isinstance(i,(list,tuple)):
            if locate(i,value):
                return True
        else:
            if i==value:
                return True
            
    return False




print(locate(['a','b',['c','d',['e']]],'a'))