#kata
#https://www.codewars.com/kata/517b0f33cd023d848d000001/train/python

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def strike(self, enemy, swings):
        # health cannot go below zero
        enemy.health = max(0, enemy.health - (swings * 10))