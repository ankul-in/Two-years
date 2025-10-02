#kata
#https://www.codewars.com/kata/5886dbc685d5788715000071/train/python

from itertools import combinations

def isComfort(num1, num2):
    summ = sum(int(i) for i in str(num1))
    return num1 - summ <= num2 <= num1 + summ

def comfortable_numbers(l, r):
       
    count = 0
    for a, b in combinations(range(l, r + 1), 2):
        if isComfort(a, b) and isComfort(b, a):
            count += 1
    return count


# from itertools import combinations_with_replacement
# def isComfort(num1,num2):
#     summ=sum(int(i) for i in str(num1))
#     if num1+summ >= num2 and num1-summ <= num2:
#         return True
#     return False

# def comfortable_numbers(l, r):
#     if l>r:
#         return "invalid"
#     list=[i for i in range(l,r)]
#     comb=[i for i in combinations_with_replacement(list,2)]
#     for i in comb:
#         if i[0]==i[1]:
#             comb.remove(i)
#         else:
#             answer.append(i) #and there are issues here
#     count=0
#     for i in comb:
#         if isComfort(i[0],i[1]):
#             count+=1  
#     return count

#print(comfortable_numbers(12,108))
#print(comfortable_numbers(10,12))
print(comfortable_numbers(1,9))