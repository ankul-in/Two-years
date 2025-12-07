#kata
#https://www.codewars.com/kata/5d076515e102162ac0dc514e/train/python

def baby_shark_lyrics():
    answer=""
    for i in ["Baby shark","Mommy shark","Daddy shark","Grandma shark","Grandpa shark","Let's go hunt"]:
        for _ in range(3):
            answer+=i+","+" doo"*6+"\n"
        answer+=i+"!\n"
    return answer+"Run away,…"