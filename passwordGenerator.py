#passwordGenerator

import random , string
def passwordGenerator(length):
        passLength=0
        password=""

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        while passLength!=length:
            password=password+random.choice(lower+upper+digits+symbols)
            passLength=len(password)
        x=[]
        for i in password:
               x.append(i)
        #print(x)       
        random.shuffle(x)
        password="".join(x)
        return print(password)
# print("enter yes if you want your password to include the following-->")
# islower=input("lowercase characters-->")
# if islower.lower()=="yes":
#         islower=True
# isupper=input("uppercase characters-->")
# if isupper.lower()=="yes":
#         isupper=True
# isdigits=input("numbric digits-->")
# if isdigits.lower()=="yes":
#         isdigits=True
# issymbols=input("symbols-->")
# if issymbols.lower()=="yes":
#         issymbols=True
length=int(input("enter number of digit you want for your password-->"))
passwordGenerator(length)

        
         