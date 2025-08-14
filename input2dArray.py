#input 2d array using np
import numpy as np
n=int(input("enter number of rows-->"))
print("enter the element row by row , seperated by space-->")
arr=np.array([list(map(int,input().split())) for i in range(n)])
print(arr)