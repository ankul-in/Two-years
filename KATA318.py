#kata
#https://www.codewars.com/kata/5768a693a3205e1cc100071f/train/python

def initialize_names(name):
    if len(name.split())<=2:
        return name
    midName=[]
    nameList=name.split()
    for i in nameList[1:-1]:
        midName.append(i[0]+".")
    return nameList[0]+" "+" ".join(midName)+" "+nameList[-1]    
    
