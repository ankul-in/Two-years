#kata https://www.codewars.com/kata/57fd696e26b06857eb0011e7/train/python
def dative(word):
    rev=word[::-1]
    for i in rev:
        if i in ("e","é", "i", "í", "ö", "ő", "ü", "ű"):
            return word+"nek"
        elif i in ("a", "á", "o", "ó", "u", "ú"):
            return word+"nak"
        else:
            continue

