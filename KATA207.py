#kata
#https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python

def land_perimeter(arr):
    answer=[]
    for x,i in enumerate(arr):
        for y,j in enumerate(i):
            if j=="X":
                answer.append((x,y))
    count=0
    for x,y in answer:
        if (x+1,y) in answer:
            count+=1
        if (x,y+1) in answer:
            count+=1
    ans=(len(answer)*4)-(count*2)
    return f"Total land perimeter: {ans}"
    

print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))
