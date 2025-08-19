#kata convert binary valuees to string https://www.codewars.com/kata/5ab3495595df9ec78f0000b4/train/python 
def binary_to_string(binary):
    lst=[]
    alphabet=[]
    binary=binary.split("0b")
    
    
    for i in binary:
        if i: #idk mat what this does
            
            x=chr(int(i,2))
            alphabet.append(x)
    return "".join(alphabet)