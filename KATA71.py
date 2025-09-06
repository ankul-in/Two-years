#kata
#https://www.codewars.com/kata/599db0a227ca9f294b0000c8/train/python

def test(r):
    
    dic={}
    average=sum(r)/len(r)
    average=round(average,3)
    print(average)
    countH=0
    countA=0
    countL=0
    for i in r:
        if i>8:
            countH+=1
        if i==7 or i==8:
            countA+=1
        if i<7:
            countL+=1
    dic["h"]=countH
    dic["a"]=countA
    dic["l"]=countL
    if len(r)==countH:
        return [average,dic,"They did well"]
    return [average,dic]
test([10,9,9,10,9,10,9])