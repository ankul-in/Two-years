#kata
#https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

def open_or_senior(data):
    answer=[]
    for i,j in data:
        if i>=55 and j>7:
            answer.append("Senior")
        else:
            answer.append("Open")
    return answer
print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))