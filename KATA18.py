from preloaded import MORSE_CODE

def decode_morse(morse_code):
    words = morse_code.strip().split("   ")  
    decoded_words = []

    for word in words:
        letters = word.split(" ")  
        decoded_letters = [MORSE_CODE[letter] for letter in letters if letter]
        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)




# from preloaded import MORSE_CODE

# def decode_morse(morse_code):
#     words=list(str(morse_code).split("   "))
#     y=""
#     for i in words:
#         letter=list(str(i).split(" "))
#         x=""
#         for j in letter:
            
#             x=x+MORSE_CODE[j]
#         y=y+x+" "
#     return y.rstrip()