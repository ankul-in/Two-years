#kata
# https://www.codewars.com/kata/598638d7f3a2c489b2000030/train/python
# 
def get_root_property(data, target):
    for key, value in data.items():
        if contains_value(value, target):
            return key
    return None  

def contains_value(node, target):
    if isinstance(node, list):
        return target in node
    elif isinstance(node, dict):
        return any(contains_value(child, target) for child in node.values())
    return False