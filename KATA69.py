#kata
#https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python


def sum_of_intervals(intervals):
    if not intervals:
        return 0
    intervals = [list(interval) for interval in intervals]
    intervals.sort(key=lambda x: x[0])
    merged=[intervals[0]]
    for i in intervals[1:]:
        last=merged[-1]
        if last[1] >= i[0]:
            last[1] = max(last[1], i[1])
        else:
            merged.append(i)
    sum=0
    for start,end in merged:
        sum=sum+(end-start)
    return sum
            
#this was soo good ngl
def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s          