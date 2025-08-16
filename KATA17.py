from collections import Counter
dic = {"1": 1000, "6": 600, "5": 500,"4": 400, "3": 300, "2": 200,"S1": 100, "S5": 50}

def score(dice):
    count = Counter(dice)
    sum = 0
    print(count)
    for num, freq in count.items():
        if freq >= 3:
            sum += dic[str(num)]
            freq -= 3  
        if num == 1:
            sum += freq * dic["S1"]
        elif num == 5:
            sum += freq * dic["S5"]
    return sum
print(score( [5, 1, 3, 4, 1] ))