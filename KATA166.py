#kata
#https://www.codewars.com/kata/5720a1cb65a504fdff0003e2/train/python

def difference_in_ages(ages):
    x=sorted(ages)
    y=x[-1]-x[0]
    return (x[0],x[-1],y)

def difference_in_ages(ages):
    x=sorted(ages)
    return (x[0],x[-1],x[-1]-x[0])

#damn min max
def difference_in_ages(ages):
    return (min(ages) , max(ages) , max(ages) - min(ages))