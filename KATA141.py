#kata
#
# def is_centered(xs: list[int], n: int) -> bool:
#     flag=False
#     for i in range(len(xs)):
#         if sum(xs[i:-i]) == n:
#             print(i,"<--i")
#             print(sum(xs[i:-i+1]),"<----sum")
#             print(xs[i-1:-i],"<---array")
#             flag=True
#     return flag
# print(is_centered([2,10,4,1,6,9],15))
# #print(is_centered([2,1,2],0))

def is_centered(xs: list[int], n: int) -> bool:
    for i in range(((len(xs)+1)//2)):
        sublist=xs[i:len(xs)-i]
        sumsub = sum(sublist) 
        if sumsub == n:
            return True
    if len(xs) % 2 == 0:
        return 0 == n
    return False
print(is_centered([25],25)) #true
print(is_centered([2,1,2],0)) #false

