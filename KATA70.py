#kata
#https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2/train/python

def direction(facing, turn):
    compass={"N":0,"NE":45,"E":90,"SE":135,"S":180,"SW":225,"W":270,"NW":315}
    x=(compass[facing]+turn)%360
    return "".join([dir for dir,deg in compass.items() if deg==x])


def direction(facing, turn):
    compass={"N":0,"NE":45,"E":90,"SE":135,"S":180,"SW":225,"W":270,"NW":315}
    compassRev = { v: k for (k, v) in compass.items() }
    x=(compass[facing]+turn)%360
    return compassRev[x]


#bestSol
DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
def direction(facing, turn):
    return DIRECTIONS[(turn // 45 + DIRECTIONS.index(facing)) % 8]