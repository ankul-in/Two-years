#kata
#https://www.codewars.com/kata/5427db696f30afd74b0006a3/train/python

def bowling_score(rolls):
    score = 0
    i = 0
    for frame in range(10):
        if rolls[i] == 10:  
            score += 10 + rolls[i+1] + rolls[i+2]
            i += 1
        elif rolls[i] + rolls[i+1] == 10:  
            score += 10 + rolls[i+2]
            i += 2
        else:  
            score += rolls[i] + rolls[i+1]
            i += 2
    return score

print(bowling_score([9, 1] * 10 + [9]))  

