import itertools 

def permutations(s):
    res=[]
    x= itertools.permutations(s)
    for i in x:
        y="".join(list(i))
        if y not in res:
            res.append(y)
    return res

# import itertools 

# def permutations(s):
#     res=list(set("".join(x) for x in itertools.permutations(s)))
#     return res
