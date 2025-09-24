#kata
#https://www.codewars.com/kata/550cc572b9e7b563be00054f/train/python


def SJF(jobs, index):
    interest=jobs[index]
    listjobs=sorted(jobs[:])
    sum=0
    for i in sorted(listjobs):
        sum+=i
        if i==interest:
            return sum
    return -1

print(SJF([3,10,20,1,2], 0))