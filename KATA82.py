#kata
#https://www.codewars.com/kata/52ec24228a515e620b0005ef/train/python

def partition_count(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1  
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            partitions[i] += partitions[i - k]
    return partitions[n]
number = 2
print(f"Number of partitions of {number} is:", partition_count(number))
