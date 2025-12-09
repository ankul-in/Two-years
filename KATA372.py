#kata
#https://www.codewars.com/kata/69347c0454f16273e13b56e8/train/python

def pick(preferred, blacklisted, options):
    labels = ["A", "B", "C"]
    valid = [(label, skill, pct) for label, (skill, pct) in zip(labels, options) if skill not in blacklisted]
    if not valid:
        return "D"  
    preferred_opts = [(label, skill, pct) for label, skill, pct in valid if skill in preferred]
    if preferred_opts:
        return max(preferred_opts, key=lambda x: x[2])[0]
    return max(valid, key=lambda x: x[2])[0]




