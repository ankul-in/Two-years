def findSum(arr,intersection):
    sum=0
    sumList={}
    listA=[]
    for i in arr:
        if i not in intersection:
            sum+=i
            listA.append(i)
        else:
            sumList.update({sum:listA})
            sum=0
            sum+=i
            listA=[]
            listA.append(i)
    sumList.update({sum:listA})
    return sumList

a = [1, 4, 5, 6, 8]
b = [2, 3, 4, 6, 9]
intersection=[]
for i in a:
    if i in b:
        intersection.append(i)

#print(intersection)

