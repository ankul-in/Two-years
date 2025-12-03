#kata
#https://www.codewars.com/kata/5aa3af22ba1bb5209f000037/train/python

import re
def solve(expr):
    tokens = re.split(r'([+\-*/])', expr)
    operands = tokens[::2]   
    operators = tokens[1::2] 
    operands.reverse()
    operators.reverse()
    result = []
    for i, op in enumerate(operands):
        result.append(op)
        if i < len(operators):
            result.append(operators[i])
    return "".join(result)

