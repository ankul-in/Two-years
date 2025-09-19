
#kata
#https://www.codewars.com/kata/5497a3c181dd7291ce000700/train/python

def diagonal_sum(array):
    sum=0
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                sum+=array[i][j]
    return sum


#this is good
def diagonal_sum(array):
    
    return sum([array[a][a] for a in range(len(array))])