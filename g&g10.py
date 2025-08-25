# https://www.geeksforgeeks.org/problems/subset-sums2234/1&selectedLang=python3


from itertools import combinations
arr=list(map(int,input("Enter elements separated by space: ").split()))
ans=[]
res=[]
for i in range(len(arr)+1):
    x=combinations(arr,i)
    ans=ans+list(x)

setans=set(ans)
for i in setans:
    res.append(sum(i))
print(res)

