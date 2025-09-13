#kata
#https://www.codewars.com/kata/55f4e56315a375c1ed000159/train/python
#still cant complete all tests cause of timeout
#will check this again after learning some algorithms ie remember 9+0=90

def pow_sum_dig_term(n):
    series=[]
    i=10
    while len(series)<n:
        print(i)
        sumofdigits=(sum(int(digit) for digit in str(i)))
        if sumofdigits <= 1:
            i += 1
            continue
        power=1
        while sumofdigits**power <=i :
            print(power)
            if sumofdigits**power == i:
                series.append(i)
                break
            power+=1
        i+=1
        
    return series[n-1]
print(pow_sum_dig_term(6))



