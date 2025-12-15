#kata
#https://www.codewars.com/kata/560a4962c0cc5c2a16000068/train/python


def eq_sum_powdig(hMax, exp):
    result = []
    for num in range(2, hMax + 1):  
        if num == sum(int(digit) ** exp for digit in str(num)):
            result.append(num)
    return result
