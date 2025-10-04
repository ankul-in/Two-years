#kata
#https://www.codewars.com/kata/56ae72854d005c7447000023/train/python

import re

def create_template(template_str):
    pattern = re.compile(r'{{\s*(\w+)\s*}}')

    def template(**kwargs):
        return pattern.sub(lambda match: str(kwargs.get(match.group(1), '')), template_str)

    return template