#kata
#https://www.codewars.com/kata/5a07e5b7ffe75fd049000051/train/python

def sorter(textbooks):
    return sorted(textbooks,key=str.casefold)

print(sorter(['Algebra', 'History', 'Geometry', 'English']))
print(sorter(['Algebra', 'history', 'Geometry', 'english']))