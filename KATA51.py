#kata
#https://www.codewars.com/kata/58e18c5434a3022d270000f2/train/python
from preloaded import ANIMALS
import re
def road_kill(photo):
    
    photo = photo.replace("=", "")
    for animal in ANIMALS:
        for direction in 1, -1:
            pat = "".join(f"{char}+" for char in animal[::direction])
            if re.fullmatch(pat, photo):
                return animal
    return "??"        
#with support of 88336074710982656 L3viathan from discord

    
        
            
            