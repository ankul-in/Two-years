#kata
#https://www.codewars.com/kata/541a354c39c5efa5fa001372/train/python
#375

def ip_to_num(ip):
    x=ip.split(".")
    a=""
    for i in x:
        a+=str(format(int(i),'08b'))
    return int(a, 2)

def num_to_ip(num):
    return '.'.join(str((num >> (8 * i)) & 0xFF) for i in reversed(range(4)))


