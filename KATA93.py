#kata
#https://www.codewars.com/kata/5aa39ba75084d7cf45000008/train/python
#fibonacci with strings 
def solve(n):
    f_list = ['0', '01']
    for i in range(2, n + 1):
        f_list.append(f_list[i - 1] + f_list[i - 2])
    return f_list[n]

print(solve(7))