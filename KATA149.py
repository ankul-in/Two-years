#kata
#https://www.codewars.com/kata/55a12bb8f0fac1ba340000aa/train/python

#not mine
def find_function(param1, param2):
    func = next((item for item in param1 if callable(item) and item.__name__ == "<lambda>"), None)
    if func is None:
        return []
    return list(filter(func, param2))

print(find_function([lambda a: a%2==0,9,3,1,0],[1,2,3,4]))