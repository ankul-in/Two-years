# #input data points for knn algorithm
# import numpy as np
# n=int(input("enter number of rows-->"))
# arr=np.array([list(map(int,input("enter data point-->").split())) for i in range(n)])
# print(arr)

import numpy as np

n = int(input("Enter number of rows --> "))
arr = []

for i in range(n):
    row = list(map(int, input(f"Enter data point {i+1} --> ").split()))
    if i == 0:
        dim = len(row)
    elif len(row) != dim:
        raise ValueError(f"Row {i+1} must have {dim} elements.")
    arr.append(row)

arr = np.array(arr)
print("Data points:\n", arr)