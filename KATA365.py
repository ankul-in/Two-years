#kata
#https://www.codewars.com/kata/55caef80d691f65cb6000040/train/python

def geometric_sequence_elements(a, r, n):
    sequence = [str(a * (r ** i)) for i in range(n)]
    return ", ".join(sequence)

