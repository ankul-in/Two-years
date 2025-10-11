#kata
#https://www.codewars.com/kata/5831c5f8ac6a11e3380002de/train/python
def min_value(arr, k):
    answer=[]
    n=len(arr)
    if n<k:
        print("invalid")
        return -1
    x = [arr[i:i+k] for i in range(len(arr) - k + 1)]
    for i in x:
        answer.append(min(i))
    return answer
print(min_value([1,-2,3,-4,5,-6,7,8],1))

def min_value(arr, n):
    return [min(arr[i:i + n]) for i in range(len(arr) - n + 1)]