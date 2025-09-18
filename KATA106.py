#kata
#https://www.codewars.com/kata/5b043e3886d0752685000009/train/python
def michael_pays(cost):
    if cost<5:
        return round(cost,2)
    elif cost <= 30:
        return round(cost-(cost/3),2)
    else:
        return round(cost - 10,2)