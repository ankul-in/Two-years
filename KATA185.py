#kata
#https://www.codewars.com/kata/596f6385e7cd727fff0000d6/solutions/python

def avg_array(arrs):
    merged=zip(*arrs)
    answer=[]
    for i in merged:
        print(i)
        answer.append(sum(i)/len(i))
    return answer

print(avg_array([[2, 3, 9, 10, 7], [12, 6, 89, 45, 3], [9, 12, 56, 10, 34], [67, 23, 1, 88, 34]]))

#well well well
# def avg_array(arrs):
#     return [sum(a)/len(a) for a in zip(*arrs)]