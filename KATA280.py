#kata
#https://www.codewars.com/kata/59fb783bab11f89202001083/solutions/python

def recycle_me(rubbish):
    l,m,n=0,0,0
    for i in rubbish:
        if i>0:
            l+=1
        if i<0:
            m+=1
        if i==0:
            n+=1
    return (l,m,n)

def recycle_me(r):
    p = sum(1 for i in r if i>0)
    g = sum(1 for i in r if i<0)
    c = sum(1 for i in r if i ==0)
    return (p,g,c)