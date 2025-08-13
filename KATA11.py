#convert decimal input to its expanded form 
def expanded_form(num):
    numStr=str(num)
    length=len(numStr)
    subString=[]
    for i , digit in enumerate(numStr):
        if digit !="0":
            zero=length-i-1
            subString.append(digit+"0"*zero)
    return "+".join(subString)
print(expanded_form(13450))


