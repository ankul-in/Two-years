#kata
#https://www.codewars.com/kata/62a933d6d6deb7001093de16/solutions/python

def get_the_vowels(word):
    answer=[]
    for i in word:
        if i in "aeiou":
            answer.append(i)
    vowel="aeiou"
    index=0
    loopCount=0
    for i in answer:
        if i == vowel[index]:
            index+=1
            if index==len(vowel):
                loopCount+=1
                index=0
    return 5*loopCount+index


#so clean :sob:
def get_the_vowels(word):
    n = 0
    for i in word:
        if i == "aeiou"[n%5]:
            n += 1
    return n