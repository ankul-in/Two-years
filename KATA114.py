#kata
#https://www.codewars.com/kata/5a34f087c5e28462d9000082/train/python
def swap_head_tail(arr):
    length = len(arr)
    mid = length // 2

    if length % 2 == 0:
        return arr[mid:] + arr[:mid]
    else:
        return arr[mid+1:] + [arr[mid]] + arr[:mid]
    
#best
def swap_head_tail(a):
    r, l = (len(a)+1)//2, len(a)//2
    return a[r:] + a[l:r] +  a[:l]