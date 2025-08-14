#PYTHON IMPLEMENTATION OF euclid's distance formula
import numpy as np
#underroot((a-b)^2)
def euclidDistance(point1,point2):
    x=np.sqrt(np.sum((np.array(point1)-np.array(point2)))**2)
    return x
point1=np.array(list(map(int,input("enter the array-->").split())))
point2=np.array(list(map(int,input("enter the array-->").split())))
print(euclidDistance(point1,point2))