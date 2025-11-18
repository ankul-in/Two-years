#kata
#https://www.codewars.com/kata/5a941f4e1a60f6e8a70025fe/train/python

def odd_ball(arr):
    try:
        odd_index = arr.index("odd")
    except ValueError:
        return False 
    for item in arr:
        if isinstance(item, int) and item == odd_index:
            return True
    return False