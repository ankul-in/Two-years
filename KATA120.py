#kata
#https://www.codewars.com/kata/58a5aeb893b79949eb0000f1/train/python

def shared_bits(a, b):
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)
    zipped = list(zip(bin_a, bin_b))
    count=0
    for i,j in zipped:
        
            if i==j=="1":
                count+=1
    return count>1
print(shared_bits(43, 77))


#best answer
def shared_bits(a, b):
    return bin(a & b).count('1') > 1