#kata
#https://www.codewars.com/kata/5a084a098ba9146690000969/train/python
def time_convert(num):
    if num<=0:
        return f"00:00"
    hours = num // 60
    minutes = num % 60
    return f"{hours:02d}:{minutes:02d}"
print(time_convert(1666))