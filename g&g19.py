#https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1&selectedLang=python3
#forgot

s=input("enter your string-->")
list1=list(s)
print(list1)

from itertools import permutations
perms=permutations(list1,4)
# print(list(perms))
# print(len(list(perms)))
result=[]
for i in list(perms):
    item="".join(i)
    result.append(item)

print(f"Permutations={result} \n and length of this list is --> {len(result)}")