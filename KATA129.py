#kata
#https://www.codewars.com/kata/550cc572b9e7b563be00054f/train/python


# def SJF(jobs, index):
#     interest=jobs[index]
#     listjobs=sorted(jobs[:])
#     sum=0
#     for i in listjobs:
#         sum+=i
#         if i==interest:
#             return sum
#     return -1

def SJF(jobs, index):
    interest = (jobs[index], index)
    indexed_jobs = sorted([(bt, i) for i, bt in enumerate(jobs)])
    total = 0
    for bt, i in indexed_jobs:
        total += bt
        if (bt, i) == interest:
            return total
    return -1

print(SJF([3, 10, 10, 20, 1, 2], 2))