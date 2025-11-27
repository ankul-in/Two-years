#kata
#https://www.codewars.com/kata/59ad7d2e07157af687000070/train/python
def sentencify(words):
    if not words:
        return "."
    first = words[0]
    first = first[:1].upper() + first[1:]
    return " ".join([first] + words[1:]) + "."
