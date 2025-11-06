#kata
#https://www.codewars.com/kata/57a73e697cb1f31dd70000d2/train/python

# from preloaded import animals, elements

animals=["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
elements=["Wood", "Fire", "Earth", "Metal", "Water"]
def chinese_zodiac(year):
    animal = animals[(year - 4) % 12]
    element = elements[((year - 4) % 10) // 2]
    return f"{element} {animal}"