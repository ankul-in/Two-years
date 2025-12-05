#kata
#https://www.codewars.com/kata/557af4c6169ac832300000ba/train/python

def remove_rotten(fruits):
    if not fruits:
        return []
    return [
        fruit.lower().replace("rotten", "") if fruit.lower().startswith("rotten") else fruit.lower()
        for fruit in fruits
    ]