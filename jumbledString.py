#jumbled string - can create puzzles and english questions
import random , string
while True:
    string=input("enter your string to get jumbled string as output-->")
    if string.lower=="exit":
        break
    else:
        if " " in string.split():
            strArray=string.split()
            print(strArray)
            random.shuffle(strArray)
            string=" ".join(strArray)
        else:
            strArray=list(string)
            print(strArray)
            random.shuffle(strArray)
            string="".join(strArray)
        # elif "\n" in string.split():
        #     strArray=string.split()
        #to add sentence in future
    
    print(string)

        

        
