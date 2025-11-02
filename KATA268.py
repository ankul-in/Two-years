#kata
#https://www.codewars.com/kata/56786a687e9a88d1cf00005d/train/python

from collections import Counter
def validate_word(word):
    normalized = word.lower()
    counts = Counter(normalized)
    frequencies = list(counts.values())
    return len(set(frequencies)) == 1

print(validate_word("abcabc"))