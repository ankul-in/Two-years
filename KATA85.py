#kata
#https://www.codewars.com/kata/66c0c135a364f5b9e286c7b5/train/python


def isLeap(year):
    return (year%4==0 and year % 100 != 0 ) or (year % 400 ==0)

def time_stamp(arr):
    monthDays=[31,28,31,30,31,30,31,31,30,31,30,31]
    totalDays=0
    for y in range(1970,arr[0]):
        totalDays += 366 if isLeap(y) else 365
    for m in range(1,arr[1]):
        if m == 2 and isLeap(arr[0]):
            totalDays += 29
        else:
            totalDays += monthDays[m-1]
    totalDays += arr[2] -1
    totalSeconds = totalDays*86400
    totalSeconds += arr[3]*3600
    totalSeconds += arr[4]*60
    totalSeconds += arr[5]
    return totalSeconds

print(time_stamp([2001, 9, 9, 1, 46, 40]))