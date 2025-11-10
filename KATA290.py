#kata
#https://www.codewars.com/kata/54d3bb4dfc75996c1c000c6d/train/python


def midpoint_sum(ints):
    total = sum(ints)
    left_sum = 0
    for i, num in enumerate(ints):
        right_sum = total - left_sum - num
        if left_sum == right_sum and i not in (0, len(ints)-1):
            return i
        left_sum += num
    return -1






# def midpoint_sum(ints):
#     sums=0
#     for i in range(len(ints)):
#         sumLeft=sum(ints[:i])
#         sumRigt=sum(ints[i+1:])
#         if sumLeft==sumRigt:
#             return i
#     return None
