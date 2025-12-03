#kata
#https://www.codewars.com/kata/57efcb78e77282f4790003d8/solutions/python

from math import ceil as ceil
def how_many_times(annual_price, individual_price):
    return ceil(annual_price/individual_price)