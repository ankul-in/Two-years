#kata
#https://www.codewars.com/kata/679e3754cb041c0685865dde/train/python
def who_is_serving(current_round: int) -> int:
    x=1
    counter=1
    while x<current_round+1:
        x+=2
        counter+=1
    if counter % 2 == 0:
        return 1
    else:
        return 2
    

#feels so dumb
def who_is_serving(current_round: int) -> int:
    return current_round - 1 & 2 or 1