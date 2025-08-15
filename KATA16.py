#tailing zeroes of factorial
def zeros(n):
    k = 1
    zero = 0
    while 5 ** k <= n:
        zero += n // (5 ** k)
        k += 1
    return zero