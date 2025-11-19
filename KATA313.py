#kata
#https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a/train/python

def solution(s: str) -> int:
    if not s:
        return 0
    removals = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            removals += 1
    return removals
