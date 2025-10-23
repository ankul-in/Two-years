#kata
#https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca/train/python

def solve(arr):
    direction=[]
    situation=[]
    answer=[]
    for i in arr:
        x=i.split()
        direction.append(x[0])
        situation.append(" ".join(x[1:]))
    revDir=["Right " if i == "Left" else "Left " if i == "Right" else "Begin " if i == "Begin" else i for i in direction][::-1]
    revDir.pop()
    revDir.insert(0,"Begin ")
    y=list(zip(revDir,situation[::-1]))
    for i,j in y:
        answer.append(i+j)
    return answer
        

print(solve(['Begin on 3rd Blvd', 'Right on First Road', 'Left on 9th Dr']))
#['Begin on 9th Dr', 'Right on First Road', 'Left on 3rd Blvd']


#well well well
DIRS = {'Left': 'Right', 'Right': 'Left'}

def solve(arr):
    lst,prevDir = [], 'Begin'
    for cmd in arr[::-1]:
        d, r    = cmd.split(' on ')
        follow  = DIRS.get(prevDir, prevDir)
        prevDir = d
        lst.append(f'{follow} on {r}')
    return lst