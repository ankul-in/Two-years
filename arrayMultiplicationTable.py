#sum using array
import numpy as np 
import tabulate 
n=int(input("enter number for continous array tables-->"))
p=input("enter number of times you want your tables to multiply ie. default=10")
if p.isdigit()==False:
    p=10
else:
    p=int(p)
for i in range(1,n+1):
    x=[]
    for j in range(1,p+1):
        x.append(j)
    numbersAre=np.array(x)
    y=numbersAre*i
    # z=y.tolist()
    # print(tabulate.tabulate(z,p,tablefmt="grdi"))
    print(y)

