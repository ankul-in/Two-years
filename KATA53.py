#kata
#https://www.codewars.com/kata/57e1857d333d8e0f76002169/train/python


#Remember you have a CHANGE dictionary to work with ;)
dict1={"penny": 0.01,
"nickel": 0.05,
"dime": 0.10,
"quarter": 0.25,
"dollar": 1.00}
def change_count(change):
    coins=change.split()
    cash=0
    for i in coins:
        cash+=dict1[i]
    return f"${cash:.2f}"