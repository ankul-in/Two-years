#kata
#https://www.codewars.com/kata/572ab0cfa3af384df7000ff8/train/python

def shuffle_it(arr,*args):
    for i,j in args:
        arr[i], arr[j] = arr[j], arr[i]
    return arr