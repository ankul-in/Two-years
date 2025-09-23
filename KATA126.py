#kata
#https://www.codewars.com/kata/5983cba828b2f1fd55000114/train/python
def odd_one(arr):
    for i in arr:
        if i%2!=0:
            return arr.index(i)
    return -1
print(odd_one([2,16,98,10,13,78]))