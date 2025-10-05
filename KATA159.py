#kata
#https://www.codewars.com/kata/526c7363236867513f0005ca/train/python


def is_leap_year(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400==0:
        return True
    return False