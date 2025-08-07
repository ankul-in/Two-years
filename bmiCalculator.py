#bmi calculator
def switchBMI(bmi):
    match bmi:
        case _ if bmi<15: #wtf is wild gaurd _
            return print("Very severely underweight")
        case _ if 15<=bmi<16:
            return print("Severely underweight")
        case _ if 16<=bmi<18.5:
            return print("Underweight")
        case _ if 18.5<= bmi <25:
            return print("Normal")
        case _ if 25<=bmi <30:
            return print("Overweight")
        case _ if 30<=bmi<35:
            return print("Moderately obese")
        case _ if 35<=bmi<40:
            return print("Severely obese")
        case _ if bmi>40:
            return print("Very severely obese")
        
print("answer a few questions and you'll be provided your given bmi")
q1=input("do you use (1)metric or (2)imperial unit for your measurements-->")
if q1.isdigit():
    q1=int(q1)
else:
    print("please enter valid input!!!")
if q1==1:
    weight=float(input("enter your weight in kg-->"))
    height=float(input("enter your height in meter-->"))
    bmi=weight/(height**2)
    switchBMI(bmi)
if q1==2:
    weight=float(input("enter your weight in lbs-->"))
    height=float(input("enter your height in inches-->"))
    bmi=703*(weight/(height**2))
    switchBMI(bmi)

