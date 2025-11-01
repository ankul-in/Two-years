#kata
#https://www.codewars.com/kata/59824f384df1741e05000913/solutions/python
from collections import Counter
def most_common(s):
    freq = Counter(s)
    indexed = [(char, freq[char], i) for i, char in enumerate(s)]
    indexed.sort(key=lambda x: (-x[1], x[2]))
    return ''.join(char for char, _, _ in indexed)

print(most_common("Hello world"))