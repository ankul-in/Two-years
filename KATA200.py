#kata
#https://www.codewars.com/kata/67330f514a2d47c019c67340/train/python
#"bcYZad"
#this one works on basic tests only idk why i suck at this
def f(s):
    answer=[]
    for i,j in enumerate(s):
        if j=="@":
            home=i
            continue
        if j!=".":
            answer.append((i,j))
    newanswer = list(map(lambda x: (abs(x[0] - home), x[1]), answer))
    
    sorted_list = sorted(newanswer)
    try:
        if sorted_list[0]==sorted_list[1]:
            return "?"
    except:
        pass
    listnew=[j for i,j in sorted_list]
    return "".join(listnew)

print(f("a..Z..b..@..c..Y..d"))




# def f(s):
#     route=[]
#     answer=[]
#     for i,j in enumerate(s):
#         if j=="@":
#             home=i
#             continue
#         if j!=".":
#             answer.append((i,j))
#         # if j=="@":
#         #     route.append(s[:i][::-1])
#         #     route.append(s[i+1:])
    
#     # for i in route:
#     #     for j in i:
#     #         if j!=".":
#     #             print(j)
#     #             if j not in answer:

#     #                 answer+=j
#     return answer
# print(f("a..Z..b..@..c..Y..d"))