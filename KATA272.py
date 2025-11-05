#kata
#https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/solutions/python

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [i for i in birds if i not in geese]

print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))