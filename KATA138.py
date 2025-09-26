#kata
#https://www.codewars.com/kata/5a33ec23ee1aaebecf000130/train/python
def count_feelings(st, arr):
    answer=[]
    strlist=set(list(st))
    for i in arr:
        wordlist=set(list(i))
        if len(st)<len(i):
            continue
        if wordlist.issubset(strlist):
            answer.append(i)
    print(answer)
    if not answer:
        return "0 feelings."
    if len(answer)==1:
        return "1 feeling."
    return f"{len(answer)} feelings."
print(count_feelings('longi', ['anger', 'awe', 'joy', 'longing', 'grief']))