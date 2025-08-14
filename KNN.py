#k nearest neighbour
import numpy as np
from collections import counter
def euclidDistance(p1,p2):
    x=np.sqrt(np.sum((np.array(p1)-np.array(p2))**2))
    return x
def KNN(data,label,test,k):
    distance=[]
    for i in range(len(data)):
        dist=euclidDistance(test,data[i])
        distance.append(dist,label[i])
    distance.sort(key=lambda x:x[0])
    nearestLabel=[label for i,label in distance[:k]]
    return counter(nearestLabel).most_common(1)[0][0]
