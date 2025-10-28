#kata
#https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python

#i dont like doing these below average questions 
def vowel_indices(word):
    answer=[]
    for i,j in enumerate(word):
        if j in "aeiouyAEIOUY":
            answer.append(i+1)
    return answer

print(vowel_indices("UNDISARMED"))