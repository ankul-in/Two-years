#https://www.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates0744/1&selectedLang=python3
#nah i'ma use loops

s = "aabbccdde"
# result = []
# prev = None
# for char in s:
#     if char != prev:
#         result.append(char)
#     prev = char
# print("".join(result))
result=[]
prev=None
for i in s:
    #result.append(i)
    if i == prev:
        result.remove(i)
    else:
        result.append(i)
    prev=i
print("".join(result))
