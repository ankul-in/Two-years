# def sum_pairs(ints, s):
#     pairs = []
    
#     for i in range(len(ints)):
#         for j in range(i + 1, len(ints)):
#             if ints[i] + ints[j] == s:
#                 pairs.append((ints[i], ints[j], j))
#     if pairs==[]:
#         return None
#     best_pair = min(pairs, key=lambda x: x[2])
#     return [best_pair[0], best_pair[1]]
def sum_pairs(ints, s):
    seen = {}
    best_index = len(ints)
    out = None

    for i, num in enumerate(ints):
        complement = s - num
        if complement in seen:
            j = i  
            if j < best_index:
                best_index = j
                out = [complement, num]
        if num not in seen:
            seen[num] = i

    return out





# from itertools import combinations
# def sum_pairs(ints, s):
#     list=[]
#     output=[]
#     smallest=-100
#     pairs=combinations(ints,2)
#     for i in pairs:
#         if i[0]+i[1]==s:
#             list.append([i[0],i[1]])
#             if i[1]<smallest:
#                 smallest=i[1]
#                 #empty output
#                 output.append([i[0],i[1]])
#         else:
#             continue

#     return output
# sum_pairs([1, 4, 8, 7, 3, 15], 8)

