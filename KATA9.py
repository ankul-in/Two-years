#KATA 9 leave the even alone and sort the odd
def sort_array(source_array):
    odd=[]
    for i in source_array:
        if i%2!=0:
            odd.append(i)
    odd=sorted(odd)
    newArray=source_array[:]
    j=0
    for index , x in enumerate(newArray):
        if x%2!=0:
            newArray[index]=odd[j]
            j+=1
        
    return newArray
print(sort_array([5,1,3]))