#kata https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca/train/python
#sign change

def count_sign_changes(arr):
    if not arr:
        return 0

    count = 0
    prev = arr[0]

    for curr in arr[1:]:
        if prev * curr < 0:
            count += 1
        if curr != 0:
            prev = curr

    return count

