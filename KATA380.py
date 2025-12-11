#kata
#https://www.codewars.com/kata/5a04133e32b8b998dc000089/train/python


def solve(arr):
    r = []
    for v in arr[::-1]:
        if not r or r[-1] < v: r.append(v)
    return r[::-1]









def solve(arr):
    answer = []
    for i,j in enumerate(arr):
        flag=False
        for k in arr[i:]:
            if j<k:
                flag=True
        if flag == True:
            pass
        else:
            if j not in answer:
                answer.append(j)
    return answer

        