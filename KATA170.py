#kata
#https://www.codewars.com/kata/5925acf31a9825d616000e74/train/python

def kill_count(counselors, jason):
    answer=[]
    for i in counselors:
        if i[1]<jason:
            answer.append(i[0])
    return answer

def kill_count(counselors, jason):
    return [x for x, y in counselors if y < jason]

counselors = [['Mo', 11], ['Sonya', 5], ['Connie', 12], ['Liu', 11], ['Connie', 1], ['Ahmed', 7], ['Bart', 7], ['Bianca', 3], ['Bruce', 9], ['Sherlock', 8], ['Faith', 10], ['Josica', 12], ['Samantha', 4], ['Max', 5]]
jason = 3
print(kill_count(counselors,jason))