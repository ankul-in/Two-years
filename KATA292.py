#kata
#https://www.codewars.com/kata/597d75744f4190857a00008d/train/python

from collections import Counter
def paint_letterboxes(start, finish):
    digits = []
    for num in range(start, finish + 1):  
        digits.extend(int(d) for d in str(num))  
    count = Counter(digits)
    return [count[d] for d in range(10)]  