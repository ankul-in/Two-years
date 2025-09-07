#kata
#https://www.codewars.com/kata/5583090cbe83f4fd8c000051/solutions/python

# def digitize(n):
#     return [int(x) for x in str(n)[::-1]]

def digitize(n):
    listN=list(str(n))
    ans=[]
    for i in listN:
        i=int(i)
        ans.append(i)
    return ans[::-1]