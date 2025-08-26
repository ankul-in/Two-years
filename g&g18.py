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
dict1={1: [1], 9: [4, 5], 14: [6, 8]}
dict2={5: [2, 3], 4: [4], 15: [6, 9]}
result=[]
# for i,j in dict1.items():
#     for k,l in dict2.items():
#         if i>k:
#             result.append(dict1[i])
#             break
#         else:
#             result.append(dict2[k])
#             break
zipAns=zip(dict1,dict2)
for i,j in list(zipAns):
    if i>j:
        result.append(dict1[i])
    else:
        result.append(dict2[j])
print(result)
