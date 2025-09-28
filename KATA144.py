#kata
#https://www.codewars.com/kata/566091b73e119a073100003a/train/python


def total_licks(env):
    total=252
    positive=False
    for i in env.values():
        if i>0:
            positive=True
        total+=i
    try:
        toughest = max(env, key=env.get)
    except:
        toughest=None
    x=f"It took {total} licks to get to the tootsie roll center of a tootsie pop."
    y=f" The toughest challenge was {toughest}."
    if positive==True:
        return x+y
    return x