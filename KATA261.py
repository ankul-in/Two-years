#kata
#https://www.codewars.com/kata/595d4823c31ba629d90000d2/train/python

from collections import Counter
def find_rarest_pepe(pepes):
    count=Counter(pepes)
    lowest=min(count.values())
    if lowest>=5:
        return "No rare pepes!"
    rarest=[i for i,j in count.items() if j==lowest]
    return rarest[0] if len(rarest) == 1 else sorted(rarest)
print(find_rarest_pepe(['Donald Trump Pepe',
                       'Melania Trump Pepe',
                       'Clown Pepe',
                       'Clown Pepe',
                       'Donald Trump Pepe']))
