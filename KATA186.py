#kata
#https://www.codewars.com/kata/57e92e91b63b6cbac20001e5/train/python

def duty_free(price, discount, holiday_cost):
    earning=(discount/100)*price
    return holiday_cost//earning

print(duty_free(12, 50, 1000))

def duty_free(price, discount, holiday_cost):
    return holiday_cost//((discount/100)*price)