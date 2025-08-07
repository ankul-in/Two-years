DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

import random
dieHeight=len(DICE_ART[1])
dieWidth=len(DICE_ART[1][1]) #111 seems fine
seperator=str("|")
die=[]
n=int(input("number of die you wanna role-->"))
for i in range(n):
    x=random.randint(1,6)
    die.append(x)
print(die)
mergedDie=[]
for i in die:
    mergedDie.append(DICE_ART[i])
#print(mergedDie)
#cant understand this && my code was making errors
dice_faces_rows = []
for row_idx in range(dieHeight):
    row_components = []
    for die in mergedDie:
        row_components.append(die[row_idx])
    row_string = seperator.join(row_components)
    dice_faces_rows.append(row_string)
width = len(dice_faces_rows[0])
dice_faces_diagram = "\n".join(dice_faces_rows)
print(dice_faces_diagram)
def roll_dice():
    diceArr=[]
    for i in range(n):
        x=random.randint(1,6)
        diceArr.append(x)
    return diceArr
matches = 0
for i in range(100000):
    if roll_dice() == die:
        matches += 1

print("Estimated Probability-->",float(matches/100000))

# ima add to this program to calculate probability of events and throw a die to corrosponding probability