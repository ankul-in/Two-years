#count number of elements in list using recursion
list=[]
def numberOfItem(list):
    counter=0
    if not list:
        return counter
    else:
        return 1 + numberOfItem(list[1:])

print(numberOfItem([1,2,3,4,5,5,6,7,8,9]))
