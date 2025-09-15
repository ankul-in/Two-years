#https://www.youtube.com/watch?v=IQgR1_OTFek

#fckin time waste

from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(max(len(partest),len(usertest))):
        try:
            if partest[i]!= usertest[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R=round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__=="__main__":
    while True:
        print("enter (yes/no)")
        ck=input("Are your Ready to test your skills --> ")
        if ck.lower()=="yes":
            test=["a paragraph is a self-contained unit of discourse in writing","my name is ankul","welcome to my git repo"]
            test1=r.choice(test)
            print("###### typing-speed #######")
            print(test1)
            print("\n\n")
            time_1=time()
            testinput=input(" Enter : ")
            time_2=time()
            print("Speed : ",speed_time(time_1,time_2,testinput)," w/sec")
            print("Error : ",mistake(test1,testinput))
        elif ck.lower()=="no":
            print("thanks for your visit !!!")
            break
        else:
            print("wrong input please enter correct input")