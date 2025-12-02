#kata
#https://www.codewars.com/kata/56445cc2e5747d513c000033/train/python

import re
def validate(message):
    pattern = r"^MDZHB \d{2} \d{3} [A-Z]+( \d{2}){4}$"
    return bool(re.match(pattern, message))

