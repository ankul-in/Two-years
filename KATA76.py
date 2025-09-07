#kata
#https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python


def is_prime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i=5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        #print(i,end="")
        i+=6
    return True

print(is_prime(746501754165710456197414517454718499))