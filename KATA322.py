#kata
#https://www.codewars.com/kata/557592fcdfc2220bed000042/train/python

def pattern(n: int) -> str:
    if n <= 0:
        return ""
    base = [str(i) for i in range(1, n + 1)]
    rows = []
    for i in range(n):
        rotated = base[i:] + base[:i]
        rows.append("".join(rotated))
    return "\n".join(rows)

