#kata
#https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python


import string

def validate_hello(greetings):
    greeting = {"hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"}
    cleaned = greetings.translate(str.maketrans('', '', string.punctuation)).lower()
    for word in cleaned.split():
        if word in greeting:
            return True
    return False

print(validate_hello('AHOJ!'))