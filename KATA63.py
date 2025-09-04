#https://www.codewars.com/kata/5250a89b1625e5decd000413/train/python
#kata to flaten array

def flatten(lst):
    ans=[]
    for i in lst:
        try:
            for j in i:
                ans.append(j)
        except:
            ans.append(i)
    return ans