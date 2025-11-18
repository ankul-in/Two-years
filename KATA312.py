#kata
#https://www.codewars.com/kata/5c556845d7e0334c74698706/train/python

def fit_in(a, b, x,y):
    suitcase_min = min(x, y)
    suitcase_max = max(x, y)
    square_max = max(a, b)
    square_sum = a + b
    return square_max <= suitcase_min and square_sum <= suitcase_max