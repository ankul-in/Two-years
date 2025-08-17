#input data points
import numpy as np
n=int(input("enter number of rows-->"))
arr=np.array([list(map(int,input("enter data point-->").split())) for i in range(n)])
print(arr)