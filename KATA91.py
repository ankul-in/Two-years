#https://www.codewars.com/kata/567d71b93f8a50f461000019/train/python
#kata

def crossover(chromosome1, chromosome2, index):
    a=chromosome1[:index]+chromosome2[index:]
    b=chromosome2[:index]+chromosome1[index:]
    return [a,b]

print(crossover( '111010000010010110011011' , '001111101110010001011000', 17))