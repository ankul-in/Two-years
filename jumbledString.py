#jumbled string - can create puzzles and english questions
import random , string
while True:
    string=input("enter your string to get jumbled string as output-->")
    if string.lower=="exit":
        break
    else:
        strArray=string.split()
        print(strArray)
        random.shuffle(strArray)
        string=" ".join(strArray)
        print(string)

        
