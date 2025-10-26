#kata
#https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python

def rps(p1, p2):
    rules={"rock":"paper","paper":"scissors","scissors":"rock"}
    if rules[p1]==p2:
        return "Player 2 won!"
    elif p1==p2:
        return "Draw!"
    else:
        return "Player 1 won!"
    
    