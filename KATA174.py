#kata
#https://www.codewars.com/kata/57d532d2164a67cded0001c7/train/python
res=\
"""6|##### 5
5|
4|# 1
3|########## 10
2|### 3
1|####### 7
"""

def histogram(results):
    y=[i for i in range(1,len(results)+1)][::-1]
    z=zip(y,results[::-1])
    answer=""
    for i,j in z:
        answer+=str(i)+"|"+"#"*j+(f" {j}" if j!=0 else "")+"\n"
    return answer
print(histogram([7,3,10,1,0,5]))