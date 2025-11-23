#kata
#https://www.codewars.com/kata/58ddffda929dfc2cae0000a5/train/python

def clonewars(kata_per_day):
    clones = [kata_per_day]  
    total_kata = 0
    total_clones = 1
    while clones:
        new_clones = []
        for i in range(len(clones)):
            ability = clones[i]
            if ability > 0:
                total_kata += ability
                total_clones += 1  
                new_clones.append(kata_per_day)  
                clones[i] -= 1  
        clones.extend(new_clones)
        clones = [c for c in clones if c > 0]
    return [total_clones, total_kata]