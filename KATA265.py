#kata
#https://www.codewars.com/kata/55d3b1f2c1b2f0d3470000a9/train/python

def highest_age(group1,group2):
    max_age={'names':[],'age':-1}
    total={}
    for person in group1+group2:
        name = person['name']
        age = person['age']
        total[name] = total.get(name, 0) + age
        if total[name] > max_age['age']:
            max_age['names'] = [name]
            max_age['age'] = total[name]
        elif total[name] == max_age['age']:
            max_age['names'].append(name)
    return sorted(max_age['names'])[0]