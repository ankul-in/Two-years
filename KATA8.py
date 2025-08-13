#KATA 8 substring of a string
def checkSubstring(a,b):
    if a in b:
        return a
    else:
        return 0

def in_array(array1, array2):
    r=[]
    for i in array1:
        for j in array2:
            r.append(checkSubstring(i,j))
            r=r.remove(0)
            # filtered = [item for item in r if item != 0]
            # r=list(set(filtered))
            r=sorted(r)
            
            
    return r