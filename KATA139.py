#kata
#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

from collections import Counter
def duplicate_count(text):
    count=0
    c=Counter(text.lower())
    for i in c.values():
        if i !=1:
            count+=1
    return count

print(duplicate_count("abcdeaB"))
    
print(duplicate_count("Indivisibilities"))

#nice one liner
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])