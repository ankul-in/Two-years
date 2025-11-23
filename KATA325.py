#kata
#https://www.codewars.com/kata/5e96332d18ac870032eb735f/train/python

import string
def custom_int(value_str: str, base: int) -> int:
    digits = string.digits + string.ascii_uppercase + string.ascii_lowercase
    if base > len(digits):
        raise ValueError(f"Base {base} too high, max supported {len(digits)}")
    value = 0
    for char in value_str:
        digit = digits.index(char)
        if digit >= base:
            raise ValueError(f"Invalid digit {char} for base {base}")
        value = value * base + digit
    return value

def womens_age(age):
    for base in range(2, 50):  
        try:
            val_20 = custom_int("20", base)
            val_21 = custom_int("21", base)
            
            if age == val_20:
                return f"{age}? That's just 20, in base {base}!"
            elif age == val_21:
                return f"{age}? That's just 21, in base {base}!"
        except ValueError:
            continue
    return None

