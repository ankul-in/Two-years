#kata
#https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python

def vaporcode(s):
    return "  ".join([i.upper() for i in s if i != " "])

print(vaporcode("Lets go to the movies"))