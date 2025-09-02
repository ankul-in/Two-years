#kata
#https://www.codewars.com/kata/557a2c136b19113912000010/train/python

def reverse_it(data):
    if isinstance(data,str):
        return data[::-1]
    elif isinstance(data, (int, float)):
        rev = str(data)[::-1]
        if '.' in rev:
            return float(rev)     
        else:
            try:
                return int(rev)
            except :
                return data
    else:
        return data