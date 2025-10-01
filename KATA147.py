#https://www.codewars.com/kata/5a39724945ddce2223000800/train/python
# kata

def total_amount_visible(topNum, numOfSides):
    bottomNum = (numOfSides + 1) - topNum
    totalDots = numOfSides * (numOfSides + 1) // 2
    return totalDots - bottomNum