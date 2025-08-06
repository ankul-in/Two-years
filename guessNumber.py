#number guessing game
import random 
number=random.randint(0,25)
print("***this is number guessing game and your tries will be counted try minimum tries***")
print("type \"\"exit\"\" to quit")
for i in range(1,50):
    x=input("enter your guess -->")

    if x.isdigit():
        y=int(x)
    elif x.lower() == "exit":
        break
    else:
        print("!!!!!try pressing an integer only!!!!!")
        continue
    if y==number:
        print("WOOOOOOHOOOO YOUR WORD WAS CORRECT-->",number)
        break
    elif y>number:
        print("HINT:try something lower!!!")  
    elif y<number:
        print("HINT:try something a bit higher!!!")  
    else:
        print("wanna try again??")
print("YOUR NUMBER WAS-->",number)
