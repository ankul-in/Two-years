#kata
#https://www.codewars.com/kata/57121e6fcdbf63eb94000e51/train/python
# from preloaded import names
# import re
# print(names)
# def sc(string):
#     for animal in names:
#             pat = "".join(f"{char}+" for char in animal)
#             if re.fullmatch(pat, photo):
#                 return animal
#     return "??" 


names=['dog', 'cat', 'bat', 'cock', 'cow', 'pig', 'fox', 'ant', 'bird', 'lion', 'wolf', 'deer', 'bear', 'frog', 'hen', 'mole', 'duck', 'goat']
# def sc(string):
#     stringlist=list(string)
#     included=[]
#     for animal in names:
#             if animal in string:
#                 included.append(animal)
#     return included
from collections import Counter

def sc(s, names=names):
    s = s.lower()
    s_count = Counter(s)
    found = []
    for animal in names:
        a_count = Counter(animal)
        if all(s_count[ch] >= a_count[ch] for ch in a_count):
            idx = min((s.index(ch) for ch in set(animal)))
            found.append((idx, animal))
    found.sort(key=lambda x: x[0])
    return [animal for _, animal in found]
print(sc('edtdenrcoclkoottogoiannnaheadgg'))
print(sc("dogcat"))