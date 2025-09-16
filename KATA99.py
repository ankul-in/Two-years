#kata
#https://www.codewars.com/kata/5a00a8b5ffe75f8888000080/train/python

#this one timeout ahhhhh 
def count_one(arr):
    max_count = 0
    count = 0
    for i in arr:
        if i == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
#print(count_one([1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]))
def replace_zero(arr):
    answer = []
    for i, j in enumerate(arr):
        if j == 0:
            temp = arr[:i] + [1] + arr[i+1:]  
            x = count_one(temp)
            answer.append((i, x))
    if not answer:
        return []
    max_val = max(x for _, x in answer)
    return max(i for i, x in answer if x == max_val)



                
print(replace_zero([1,1,1,0,1,1,0,1,1,1]))
