#kata
#https://www.codewars.com/kata/55c9172ee4bb15af9000005d/train/python

# def penta_fib(n):
#     arr=[0,1,1,2,4]
#     for i in range(5,n+1):
#         arr.append(arr[-1]+arr[-2]+arr[-3]+arr[-4]+arr[-5])
#     return arr

# def count_odd_penta_fib(n):
#     if n <= 0:
#         return 0
#     setarr=set(penta_fib(n))
#     answer=[]
#     for i in setarr:
#         if i % 2 != 0:
#             answer.append(i)
#     return len(answer)    

# # def penta_fib(n):
# #     arr = [0, 1, 1, 2, 4]
# #     for i in range(5, n + 1):
# #         arr.append(sum(arr[-5:]))
# #     return arr

# # def count_odd_penta_fib(n):
# #     return sum(1 for x in set(penta_fib(n)) if x % 2 != 0)


# def count_odd_penta_fib(n):
#     if n == 0:
#         return 0
#     arr = [0, 1, 1, 2, 4]
#     for i in range(5, n + 1):
#         arr.append(sum(arr[-5:]))
#     return sum(1 for x in set(arr) if x % 2 != 0)


def count_odd_penta_fib(n):
    arr = [0, 1, 1, 2, 4]
    counter=1
    for i in range(5, n + 1):
        arr.append(sum(arr[-5:]))
        if arr[-1] % 2 != 0:
            counter+=1
        #arr.pop(0)
    return counter


    
print(count_odd_penta_fib(68))
