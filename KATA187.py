#kata
#https://www.codewars.com/kata/5921c0bc6b8f072e840000c0/train/python



def sequence_classifier(arr):
    prev=arr[0]
    answer=[]
    for i in arr[1:]:
        answer.append(i-prev)
        prev=i
    posit=0
    neget=0
    flag=0
    
    for i in answer:
        if i>0:
            posit+=1
        if i==0:
            flag+=1
        if i<0:
            neget+=1
    if posit==len(arr)-1:
        return 1
    if neget==len(arr)-1:
        return 3
    elif flag==len(arr)-1:
        return 5
    elif flag>0:
        if posit==0:
            return 4
        if neget==0:
            return 2
    return 0




# def sequence_classifier(arr):
#     diffs = [j - i for i, j in zip(arr, arr[1:])]
#     posit = sum(d > 0 for d in diffs)
#     neget = sum(d < 0 for d in diffs)
#     flag = sum(d == 0 for d in diffs)

#     n = len(arr) - 1
#     if posit == n:
#         return 1
#     if neget == n:
#         return 3
#     if flag == n:
#         return 5
#     if flag > 0:
#         if posit == 0:
#             return 4
#         if neget == 0:
#             return 2
#     return 0

#this on is so organised love it
def sequence_classifier(arr):
    if all(arr[i] == arr[i+1] for i in range(len(arr)-1)): return 5
    if all(arr[i] <  arr[i+1] for i in range(len(arr)-1)): return 1
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)): return 2
    if all(arr[i] >  arr[i+1] for i in range(len(arr)-1)): return 3
    if all(arr[i] >= arr[i+1] for i in range(len(arr)-1)): return 4
    return 0