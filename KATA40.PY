#kata



def replaceMidWord(word):
    if len(word)<=3:
        return word
    else:
        length=len(word)-2
    return word[0]+str(length)+word[-1]
        
def abbreviate(s):
    newS=""
    word=""
    for i in s:
        if i.isalpha():
            word+=i      
              
        else:
            if word:
                newS+=replaceMidWord(word)
                word=""
            newS+=i
    if word:
        newS+=replaceMidWord(word)        
            
        
    return newS

print(abbreviate("hello my1 name ihfs bruhh"))
