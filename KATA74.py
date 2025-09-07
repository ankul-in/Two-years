#kata
#https://www.codewars.com/kata/5574940eae1cf7d520000076/train/python
#odd ladder


def pattern(n: int) -> str:
    if n<=0:
        return ""
    if n % 2 == 0:
        n -= 1

    lines = []
    for i in range(1, n + 1, 2):
        lines.append(str(i) * i)

    return "\n".join(lines)

print(pattern(4))