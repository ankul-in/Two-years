#kata
#https://www.codewars.com/kata/57faf32df815ebd49e000117/train/python

def remove(text):
    return " ".join(word.rstrip("!") for word in text.split(" "))

