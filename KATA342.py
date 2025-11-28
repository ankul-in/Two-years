#kata
#https://www.codewars.com/kata/657e578bdc80170abd4dca79/train/python

def minimum_percentage(food_percentages):
    n = len(food_percentages)
    total = sum(food_percentages)
    return max(0, total - (n-1)*100)

