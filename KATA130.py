#kata
#https://www.codewars.com/kata/5deeb1cc0d5bc9000f70aa74/train/python


def zombie_shootout(zombies, distance, ammo):
    number_zombies=zombies
    for i in range(0,2*max(distance,ammo)):
        if zombies==0:
            return f"You shot all {number_zombies} zombies."
        zombies-=1
        
        if distance==0:
            return f"You shot {number_zombies-zombies-1} zombies before being eaten: overwhelmed."
        distance-=0.5
        
        if ammo==0:
            return f"You shot {number_zombies-zombies-1} zombies before being eaten: ran out of ammo."
        ammo-=1