#kata https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
def find_average(numbers):
    sum=0
    if len(numbers)==0:
        return 0
    else:
        for i in (numbers):
            sum+=i
        return sum/len(numbers)
    pass