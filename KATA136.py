# #kata
# #https://www.codewars.com/kata/68b0064510c5854a66e6323a/train/python
# def maximum_seating(lst):
#     res = 0
#     for i in range(len(lst)):
#         if sum(lst[i-2-len(lst):i+3]) == 0:
#             lst[i] = 1
#             res += 1
#     return res

# print(maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))

# from collections import deque

# cnt = 0

# seats = [0,0,0,0]

# current = deque([0, 0], 5)
# current_length = 2

# for seat in seats:
#     current.append(seat)
    
#     if current_length < 5:
#         current_length += 1
#     elif sum(current) == 0:
#         cnt += 1
        
#         current[2] = 1
# print(cnt)


# from collections import deque

# def maximum_seating(lst):
#     cnt = 0

#     seats = lst

#     current = deque([0, 0], 5)

#     for seat in seats:
#         current.append(seat)

#         if len(current) == 5 and sum(current) == 0:
#             cnt += 1

#             current[2] = 1
        
#     current.extend([0, 0])

#     if sum(current) == 0:
#         cnt += 1

#         current[2] = 1
        
#     return cnt

def maximum_seating(lst):
    s = ''.join(str(num) for num in lst)
    return sum(max((len(x) - 2) // 3, 0) for x in ('00' + s + '00').split('1'))


print(maximum_seating([0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]))