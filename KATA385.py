#kata
#https://www.codewars.com/kata/59e1b9ce7997cbecb9000014/train/python

def cog_RPM(cogs):
    rpm = 1.0
    for i in range(len(cogs) - 1):
        rpm = -rpm * (cogs[i] / cogs[i+1])
    return rpm

