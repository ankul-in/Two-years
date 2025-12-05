#kata
#https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1/train/python

def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0:
        return None
    oldest = (sum_ + difference) / 2
    youngest = (sum_ - difference) / 2
    if oldest < 0 or youngest < 0:
        return None

    return (oldest, youngest)



