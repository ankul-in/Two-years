#kata
#https://www.codewars.com/kata/59de795c289ef9197f000c48/train/python

def remove_bmw(string):
    if isinstance(string,str):
        answer=""
        for i in string:
            if i not in "bmwBMW":
                answer+=i
        return answer
    
    else:
        raise TypeError("This program only works for text.")
    
print(remove_bmw("bmwvolvoBMW"))