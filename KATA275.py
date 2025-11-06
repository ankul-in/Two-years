
#kata
#https://www.codewars.com/kata/536c00e21da4dc0a0700128b/train/python

def get_villain_name(birthdate): 
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    first_name = first[birthdate.month-1]
    last_digit = birthdate.day % 10
    last_name = last[last_digit]

    return f"{first_name} {last_name}"

