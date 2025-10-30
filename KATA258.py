#kata
#https://www.codewars.com/kata/5a63948acadebff56f000018/train/python
def max_product(lst, n):
    lst.sort(reverse=True)
    result = 1
    for i in range(n):
        result *= lst[i]
    return result

max_product([13,12,-27,-302,25,37,133,155,-1])