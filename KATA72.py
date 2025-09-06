#kata

#https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python

# import re
# def solve_runes(runes):
#     runes.replace("=","==")
#     for i in range(10):
#         x=runes.replace("?",str(i))
#         try:
#             if eval(x):
#                 return i
#         except:
#             pass
#     return -1

# solve_runes("123*45?=5?088")

import re

def solve_runes(runes):
    runes = runes[::-1].replace('=', '==', 1)[::-1]
    known_digits = set(re.sub(r'[^0-9]', '', runes))
    for digit in map(str, range(10)):
        if digit in known_digits:
            continue
        candidate = runes.replace('?', digit)
        tokens = re.split(r'[+\-*==]', candidate)
        for token in tokens:
            if token == '':
                continue
            if token.startswith('-'):
                token = token[1:]
            if len(token) > 1 and token.startswith('0'):
                break
        else:
            try:
                if eval(candidate):
                    return int(digit)
            except:
                continue

    return -1

