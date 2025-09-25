#kata
#https://www.codewars.com/kata/54a0689443ab7271a90000c6/train/python

class Harshad:
    @staticmethod
    def is_valid(number):
        sumNum=sum([int(x) for x in list(str(number))])
        return number % sumNum == 0

    @staticmethod
    def get_next(number):
        number+=1
        while True:
            sumNum=sum([int(x) for x in list(str(number))])
            if number % sumNum == 0:
                return number
            number+=1

    @staticmethod
    def get_series(count, start=0):
        number=start+1
        answer=[]
        while len(answer) != count:
            sumNum=sum([int(x) for x in list(str(number))])
            if number % sumNum == 0:
                answer.append(number)
            number+=1
        return answer

print(Harshad.get_next(67))