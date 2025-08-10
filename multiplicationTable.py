#generate multiplication table
numbersAre=[1,2,3,4,5,6,7,8,9,10]
# print("enter : before number to print tables upto that number")
# n=input("enter numbers to print their table-->")
# for i in n:
#     if i==":":
#         y=list(n)
#         y[1:]
#         y="".join(y)
#         n=int(y)
#         for i in range(n):
#             for i in numbersAre:
#                 print(n,"times",numbersAre[i],"is",n*numbersAre[i])
        
#     elif n.isdigit()==True:
#         n=int(n)
#         for i in numbersAre:
#             print(n,"times",numbersAre[i],"is",n*numbersAre[i])
#     else:
#         print("please input valide value")

continous=input("enter \"YES\" if you want continous multiplications-->")
if continous.lower()=="yes":
    continous=True
n=int(input("enter numbers to print their table-->"))
if continous==True:
    #for i in range(n):
        # for j in numbersAre:
        #     print(i,"times",numbersAre[j],"is",n*numbersAre[j])
    for i in range(1,n+1):
        for j in numbersAre:
            print(i,"*",j,"=",i*j)
else:
    for j in numbersAre:
        print(n,"*",j,"=",j*n)
