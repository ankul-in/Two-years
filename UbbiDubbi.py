#https://www.youtube.com/watch?v=qglQloYv82Q
def ubbiDubbiTranslate(word):
    if not word.isalpha():
        return word
    newWord=""
    for i in word:
        if i.lower() in "aeiou":
            newWord+="ab"+i
        else:
            newWord+=i
    
    return newWord
def ubbiDubbiDeTranslate(word):
    # try:
    #     return word.replace("ab","")
    # except:
    #     return word
    return word.replace("ab","")
def convertUBBI(sentence):
    # newsentence=""
    # for i in sentence.strip():
    #     newsentence += ubbiDubbiTranslate(i) 
    # return newsentence
    words = sentence.strip().split()
    translated = [ubbiDubbiTranslate(word) for word in words]
    return " ".join(translated)


def ubbiDubbiDeSentence(sentence):
    # newsentence=""
    # for i in sentence.strip():
    #     newsentence += ubbiDubbiDeTranslate(i) 
    # return newsentence
    words = sentence.strip().split()
    detranslated = [ubbiDubbiDeTranslate(word) for word in words]
    return " ".join(detranslated)

print(ubbiDubbiDeTranslate("whaberabe"))
print(ubbiDubbiDeSentence("whaberabe abarabe yaboabu gaboabing maban"))
print(ubbiDubbiDeTranslate(ubbiDubbiTranslate("cat")))
print(ubbiDubbiDeTranslate("you"))

