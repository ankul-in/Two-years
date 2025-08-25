#https://www.geeksforgeeks.org/problems/combination-sum-1587115620/1&selectedLang=python3

def makeCombination(arr,remSum,cur,res,index):
    if remSum==0:
        res.append(list(cur))
        return
    if remSum<0 or index>=len(arr):
        return
    cur.append(arr[index])
    makeCombination(arr,remSum - arr[index],cur,res,index)
    cur.pop()
    makeCombination(arr,remSum,cur,res,index+1)

def combinationSum(arr,target):
    arr.sort()
    cur=[]
    res=[]
    makeCombination(arr,target,cur,res,0)
    return res
if __name__=="__main__":
    arr=[2,4,6,8]
    target=8
    res=combinationSum(arr,target)
    for v in res:
        print(" ".join(map(str,v)))