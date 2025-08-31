#kata
#https://www.codewars.com/kata/559f89598c0d6c9b31000125/train/python


def archers_ready(archers):
    if not archers:
        return False
    for i in archers:
        if i>=5:
            pass
        else:
            return False
    return True