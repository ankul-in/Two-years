#https://www.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1&selectedLang=python3
import math
def deleteMid(arr):
    size=len(arr)
    index=math.floor((size+1)/2)
    arr.remove(index)
    return arr
# def deleteMid(s,current=0):
#     if not s:
#         return
#     mid=len(s)//2
#     if current==mid:
#         s.pop()

#         return
#     top=s.pop()
#     deleteMid(s,current+1)
#     s.append(top)


s = [1, 2, 3, 4, 5]
deleteMid(s)
print(s)

