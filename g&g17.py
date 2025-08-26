from itertools import combinations

n=5
friends=[]
for i in range(n):
    friends.append(i)

comb=combinations(friends,1)
comb2=combinations(friends,2)
setF=set()

for c in comb:
    setF.add((c))

for c in comb2:
    setF.add((c))
# l=list(setF)
# setFinal=l[::-1]
print(setF)
single=[]
couple=[]
for i in setF:
    if len(i)<2:
        couple.append(i)
    else:
        single.append(i)

print(single)
print(couple)