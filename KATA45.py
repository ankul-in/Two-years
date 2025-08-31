#kata


# def isomorph(a, b):
#     if len(a)!=len(b):
#         return False
#     mappingA={}
#     mappingB={}
#     for i,j in zip(a,b):
#         if i in mappingA:
#             if mappingA.get(i)!=j:
#                 return False
#         else:
#             mappingA[i]=j
#         if i in mappingB:
#             if mappingB.get(i)!=j:
#                 return False
#         else:
#             mappingB[i]=j
#     return True

def isomorph(a, b):
    if len(a)!=len(b):
        return False
    mappingA={}
    mappingB={}
    for i,j in zip(a,b):
        if mappingA.get(i,j) != j or mappingB.get(j,i) != i:
            return False
        mappingA[i] = j
        mappingB[j] = i


    return True