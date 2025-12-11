#kata
#https://www.codewars.com/kata/57a6633153ba33189e000074/train/python

def ordered_count(s):
    result = []
    seen = set()
    for ch in s:
        if ch not in seen:
            result.append((ch, s.count(ch)))
            seen.add(ch)
    return result

