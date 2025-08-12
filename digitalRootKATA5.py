## yeah this is digital root program
# def digit_sum(n):
#   s = 0
#   while n > 0:
#     s += n%10
#     n //= 10
#   return s
# def digital_root(n):
#   while n > 9:
#     n = digit_sum(n)
#   return n
def digitSum(n):
    if n<=10:
        return n 
    else:
        return digitSum(sum(map(int,str(n))))