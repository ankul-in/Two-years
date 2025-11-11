#kata
#https://www.codewars.com/kata/57eeb8cc5f79f6465a0015c1/train/python

def is_kiss(text):
    words = text.split()
    word_count = len(words)
    for word in words:
        if len(word) > word_count:
            return "Keep It Simple Stupid"
    return "Good work Joe!"