#kata
#https://www.codewars.com/kata/68a41d2d72e334f5d4c957a2/train/python
def minimum_value(coefficients, target):
    lambda_squared_sum = sum(l**2 for l in coefficients)
    if lambda_squared_sum == 0:
        raise ValueError("Sum of squares of coefficients cannot be zero.")
    return (target ** 2) / lambda_squared_sum

print(minimum_value("3a+4b=5"))
#ima check this again