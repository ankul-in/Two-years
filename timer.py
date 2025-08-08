#timer
import time
def counter(t):
    while t!=0:
        mins,secs=divmod(t,60)
        timer="{:02d}:{:02d}".format(mins,secs)#2d=2decimal
        print(timer,end="\r")
        time.sleep(1) #pauses execution for 1 second
        t=t-1
    print("that was your time",x,"seconds")
t=int(input("enter timer(in sec)")) 
x=t  
counter(t)

