#kata
#https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python


def solution(array_a, array_b):
    x=zip(array_a,array_b)
    y=sum([abs(i[0]-i[1])**2 for i in x])
    return y/len(array_a)

print(solution([1,2,3],[4,5,6]))