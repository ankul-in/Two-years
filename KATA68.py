#kata
#https://www.codewars.com/kata/559af787b4b8eac78b000022/train/python

#     # def count_me(data):
#     #     if not data or not data.isdigit():
#     #         return ""
#     #     counter=0
#     #     answer=[]
#     #     set1=set()
#     #     for i in data:
            
#     #         for j in data:
#     #             if j in set1:
#     #                 continue
#     #             if i==j:
#     #                 counter+=1
#     #         if counter==0:
#     #             continue
#     #         answer.append(str(counter))
#     #         answer.append(str(i))
#     #         counter=0
#     #         set1.add(i)
#     #     return "".join(answer)


# def count_me(data):
#     if not data or not data.isdigit():
#         return ""
#     result=[]
#     prev=data[0]
#     counter=1
#     for i in data[1:]:
#         if prev==i:
#             counter+=1
#         else:
#             result.append(str(counter))
#             result.append(str(i))
#             counter=1
#     result.append(str(counter))
#     result.append(prev)


#     return "".join(result)


# def count_me(data):
#     if not data or not data.isdigit():
#         return ""
    
#     result = []
#     prev = data[0]
#     counter = 1

#     for i in data[1:]:
#         if i == prev:
#             counter += 1
#         else:
#             result.append(str(counter))
#             result.append(prev)
#             prev = i
#             counter = 1

#     # Append the last group
#     result.append(str(counter))
#     result.append(prev)

#     return "".join(result)

def count_me(data):
    if not data or not data.isdigit():
        return ""
    result=[]
    prev=data[0]
    counter=1
    for i in data[1:]:
        if prev==i:
            counter+=1
        else:
            result.append(str(counter))
            result.append(prev)
            prev=i
            counter=1
            
    result.append(str(counter))
    result.append(prev)


    return "".join(result)