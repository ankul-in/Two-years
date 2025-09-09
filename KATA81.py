#kata
#https://www.codewars.com/kata/55b8c0276a7930249e00003c/train/python

from preloaded import CHAR_TO_MORSE
def encryption(string):
    ans=[]
    for char in string:
        if char==" ":
            ans.append("  ")
        morse=CHAR_TO_MORSE.get(char.upper())
        if morse:
            ans.append(morse)
            ans.append(" ")
        
    return "".join(ans).strip()