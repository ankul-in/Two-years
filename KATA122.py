#kata
#https://www.codewars.com/kata/5bd00c99dbc73908bb00057a/train/python

def alpha_seq(strng):
    answer=[]
    l1=sorted(list(strng.upper()))
    
    for i in l1:
        loop=ord(i)-65
        x=i.lower()*loop
        answer.append(str(i+x))
        
    return ",".join(answer)


print(alpha_seq("ZpglnRxqenU"))