#kata
#https://www.codewars.com/kata/53d16bd82578b1fb5b00128c/train/python


def grader(score):
    match score:
        case _ if score>1 or score<0.6:
            return "F"
        case _ if score>=0.9:
            return "A"
        case _ if score>=0.8:
            return "B"
        case _ if score>=0.7:
            return "C"
        case _ if score>=0.6:
            return "D"
        

print(grader(1))