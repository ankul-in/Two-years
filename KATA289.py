#kata
#https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python
def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    result = []
    a, b = max(lng, wdth), min(lng, wdth)
    while b:
        count = a // b
        result.extend([b] * count)
        a, b = b, a % b
    return result





# def sq_in_rect(lng, wdth):
#     if lng == wdth:
#         return None
#     answer = []
#     while lng != wdth:
#         if lng > wdth:
#             answer.append(wdth)
#             lng -= wdth
#         else:
#             answer.append(lng)
#             wdth -= lng
#     answer.append(lng)  
#     return answer




