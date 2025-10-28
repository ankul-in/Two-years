#kata
#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    answer=[]
    wordlist=sentence.split()
    for j in (wordlist):
        if len(j)>=5:
            answer.append(j[::-1])
        else:
            answer.append(j)
    return " ".join(answer)