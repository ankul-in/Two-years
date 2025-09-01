#kata
#https://www.codewars.com/kata/55b54be931e9ce28bc0000d6/train/python



# Given the number of consecutive integers and the total of the integers,
# return the consecutive integer at the requested position.
#
# Input: 
#    x number of consecutive integers
#    y sum of consecutive integers
#    n position of requested integer
#
# return integer at requested position

def position(n, total_sum, index):
    ans = []
    a = (total_sum - (n * (n - 1) // 2)) / n
    for i in range(n):
        ans.append(a)
        a += 1
    return ans[index]

