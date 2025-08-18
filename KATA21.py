"""KATA21 Your task is to write an update for a lottery machine. 
Its current version produces a sequence of random letters and integers (passed as a string to the function). 
Your code must filter out all letters and return unique integers as a string, in their order of first appearance. 
If there are no integers in the string return "One more run!"
"""

def lottery(s):
    digit=[]
    x=list(s)
    for i in x:
        if i.isdigit():
            if i not in digit:
                digit.append(i)
    if not digit:
        return "One more run!"
    return "".join(digit)
    
#wohoooh