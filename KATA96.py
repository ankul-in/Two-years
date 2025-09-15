#kata
#https://www.codewars.com/kata/55c353487fe3cc80660001d4/train/python


def capitals_first(text):
    answer=[]
    for i in text.split():
        if i[0].isupper():
            answer.append(i)
    for i in text.split():
        if i[0].islower():
            answer.append(i)
    return " ".join(answer)

print(capitals_first("sense Does to That Make you?"))

def capitals_first(string):
    return ' '.join([word for word in string.split() if word[0].isupper()] + [word for word in string.split() if word[0].islower()])
    