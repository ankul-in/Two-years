#kata
#https://www.codewars.com/kata/633a870b198a4c00286ad2b7/solutions/python

from datetime import date , timedelta
def life_predictor(datex):
    date1=date.fromisoformat(datex)
    x=date1-timedelta(days=280)
    return x.isoformat()
print(life_predictor("2000-01-01"))