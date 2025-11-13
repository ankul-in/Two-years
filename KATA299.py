#kata
#https://www.codewars.com/kata/55805ab490c73741b7000064/train/python
dictionary={'A': 'awesome', 'B': 'beautiful', 'C': 'confident', 'D': 'disturbing', 'E': 'eager', 'F': 'fantastic', 'G': 'gregarious', 'H': 'hippy', 'I': 'ingestable', 'J': 'joke', 'K': 'klingon', 'L': 'literal', 'M': 'mustache', 'N': 'newtonian', 'O': 'oscillating', 'P': 'perfect', 'Q': 'queen', 'R': 'rant', 'S': 'stylish', 'T': 'turn', 'U': 'underlying', 'V': 'volcano', 'W': 'weird', 'X': 'xylophone', 'Y': 'yogic', 'Z': 'zero'}


def make_backronym(string):
    return ' '.join(dictionary[char.upper()] for char in string)