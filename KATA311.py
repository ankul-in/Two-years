#kata
#https://www.codewars.com/kata/56f3f6a82010832b02000f38/train/python

def describe_age(a):
    return "You're a(n) " + ["kid", "teenager", "adult", "elderly"][(a > 12) + (a > 17) + (a > 64)]