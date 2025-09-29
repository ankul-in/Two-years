#kata
#https://www.codewars.com/kata/584d2c19766c2b2f6a00004f/train/python
# def func_or(a,b):
#     if a == True:
#         if b == False:
#             return True
#     if b == True:
#         if a == False:
#             return True
#     return False

# def func_xor(a,b):
#     if a == True:
#         return True
#     if b == True:
#         return True
#     return False

def func_xor(a, b):
    if bool(a) != bool(b):
        return True
    return False

def func_or(a, b):
    if bool(a) or bool(b):
        return True
    return False



print(func_or(True, True))