#kata
#https://www.codewars.com/kata/6630da20f925eb3007c5a498/train/python

def blow_candles(candles: str) -> int:
    arr = [int(c) for c in candles]
    blows = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            i += 1
            continue
        for j in range(i, min(i+3, len(arr))):
            if arr[j] > 0:
                arr[j] -= 1
        blows += 1
    return blows



