#kata
#https://www.codewars.com/kata/5a58d889880385c2f40000aa/solutions/python

def automorphic(n):
    square=n*n
    if str(square).endswith(str(n)):
        return "Automorphic"
    else:
        return "Not!!"