#k nearest neighbour
import numpy as np
from collections import Counter
def euclidDistance(p1,p2):
    x=np.sqrt(np.sum((np.array(p1)-np.array(p2))**2))
    return x
def KNN(data,label,test,k):
    distance=[]
    for i in range(len(data)):
        dist=euclidDistance(test,data[i])
        distance.append((dist,label[i]))
    distance.sort(key=lambda x:x[0])
    nearestLabel=[label for i,label in distance[:k]]
    return Counter(nearestLabel).most_common(1)[0][0]
training_data = [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8]]
training_labels = ['A', 'A', 'A', 'B', 'B']
test_point = [4, 5]
k = 3
prediction = KNN(training_data, training_labels, test_point, k)
print(prediction)