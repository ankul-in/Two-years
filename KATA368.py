#kata
#https://www.codewars.com/kata/6834f1a80e0a48c2ea3feeb0/train/python

import re
def i_before_e(word):
    pattern = re.compile(r"[ie]+")
    def replacer(match):
        seq = match.group()
        i_count = seq.count("i")
        e_count = seq.count("e")
        start = match.start()
        preceding_char = word[start - 1] if start > 0 else ""
        if preceding_char == "c":
            return "e" * e_count + "i" * i_count
        else:
            return "i" * i_count + "e" * e_count
    
    return pattern.sub(replacer, word)

