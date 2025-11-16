#kata
#https://www.codewars.com/kata/563a8656d52a79f06c00001f/train/python

import re
def is_valid(s: str) -> bool:
    pattern = re.compile(r'^[A-Za-z_$][A-Za-z0-9_$]*$')
    return bool(pattern.match(s))


