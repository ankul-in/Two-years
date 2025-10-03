#kata
#https://www.codewars.com/kata/544e2c60908f2da03600022a/train/python
import math
def degrees(rad):
    n=(rad/math.pi)*180
    return f"{int(n)}deg" if n == int(n) else f"{round(n, 2)}deg"

def radians(deg):
    n=(deg*math.pi)/180
    return f"{int(n)}rad" if n == int(n) else f"{round(n, 2)}rad"

print(degrees(40.840704496667314))
print(degrees(47.12388980384689))