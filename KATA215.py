#kata
#https://www.codewars.com/kata/67fb86b6564f0bd70dc615b1/train/python
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
def validate_euro(serial_number):
    if serial_number[0].islower() or serial_number[1].islower():
        False
    listD=[int(i) for i in serial_number[2:]]
    print(listD)
    valid=sum(listD)+(ord(serial_number[0])-64+ord(serial_number[1])-64)
    return digital_root(valid)==7

print(validate_euro("VA0436214792"))