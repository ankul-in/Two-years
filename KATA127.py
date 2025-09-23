#kata
#https://www.codewars.com/kata/5889177bf148eddd150002cc/train/python

# def tiy_fizz_buzz(string):
#     vowel="aeiouAEIOU"
#     for i in string:
#         if i in vowel:
#             if i == i.upper():
#                 return string.replace(i,"Iron Yard")
#             return string.replace(i,"Yard")
#         if i == i.upper():
#             return string.replace(i,"Iron")
#         return string
# print(tiy_fizz_buzz("A"))   
def tiy_fizz_buzz(string):
    vowel = "aeiouAEIOU"
    result = ""
    for i in string:
        if i in vowel:
            if i.isupper():
                result += "Iron Yard"
            else:
                result += "Yard"
        elif i.isalpha():
            if i.isupper():
                result += "Iron"
            else:
                result += i
        else:
            result += i
    return result
print(tiy_fizz_buzz('IronYardllYard IronIron YardIronIronIron!'))
