#kata
#https://www.codewars.com/kata/585eaef9851516fcae00004d/train/python

def what_list_am_i_on(actions):
    naughty,nice=0,0
    for i in actions:
        if i[0] in "bfkBFK":
            naughty+=1
        elif i[0] in "gsnGSN":
            nice+=1
    if naughty>=nice:
        return "naughty"
    return "nice"