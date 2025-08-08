#passwordGenerator

import random , string
def passwordGenerator(length):
        passLength=0
        password=""

        if islower.lower()=="yes":
               lower = string.ascii_lowercase
        else:
               lower=""
        if isupper.lower()=="yes":
               upper = string.ascii_uppercase
        else:
               upper=""
        if isdigits.lower()=="yes":
               digits = string.digits
        else:
               digits=""
        if issymbols.lower()=="yes":
                symbols = string.punctuation
        else:
               symbols=""
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
print("enter yes if you want your password to include the following-->")
islower=input("lowercase characters-->")
#islower=False
#if islower.lower()=="yes":
#        islower=True
isupper=input("uppercase characters-->")
#isupper=False
#if isupper.lower()=="yes":
#         isupper=True
isdigits=input("numbric digits-->")
#isdigits=False
#if isdigits.lower()=="yes":
#        isdigits=True
issymbols=input("symbols-->")
#issymbols=False
#if issymbols.lower()=="yes":
#        issymbols=True
length=int(input("enter number of digit you want for your password-->"))
passwordGenerator(length)

        
         