#kata
#https://www.codewars.com/kata/545f05676b42a0a195000d95/train/python

# def ranks(a):
#     if not a:
#         return []
#     listSorted = sorted(set(a))
#     indexedDict = {value: index for index, value in enumerate(listSorted,start=1)}
#     return [indexedDict[i] for i in a]
#array = [3,3,3,3,3,5,1] --> ranks = [2,2,2,2,2,1,7]
def ranks(a):
    if not a:
        return []
    listSorted = sorted(a,reverse=True)
    print(listSorted)
    #indexedDict = {value: index for index, value in enumerate(listSorted,start=1)}
    indexedDict = {}
    for index, value in enumerate(listSorted, start=1):
        if value not in indexedDict:
            indexedDict[value] = index
    print(indexedDict)
    return [indexedDict[i] for i in a]
    
    
print(ranks([3,3,3,3,3,5,1]))

#damn psychos
def ranks(a):
  sortA = sorted(a, reverse=True)
  return [sortA.index(s) + 1 for s in a]