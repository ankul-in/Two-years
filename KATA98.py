#kata
#https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
# def up_array(arr):
#     strArr=[str(i) for i in arr]
#     x="".join(strArr)
#     y=len(x)
#     x=int(x)+1
#     result=[int(i) for i in str(x)]
#     if len(result)!=y:
#         result.insert(0,0)
#         return result
#     return result

# def up_array(arr, length=None):
#     if not arr or any(x < 0 or x > 9 for x in arr):
#         return None
#     num = int(''.join(map(str, arr)))
#     incremented = num + 1
#     return [int(digit) for digit in str(incremented)]

def up_array(arr):
    if not arr or any(x < 0 or x > 9 for x in arr):
        return None
    result = arr[:]
    carry = 1
    for i in range(len(result) - 1, -1, -1):
        total = result[i] + carry
        result[i] = total % 10
        carry = total // 10
    if carry:
        result = [carry] + result
    return result
print(up_array([9,9]))
print(up_array([0,2,9]))
#this sucks
