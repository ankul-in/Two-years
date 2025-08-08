#shut down and restart program
import os 
from plyer import notification
def shutdown():
    notification.notify(message="YOUR SYSTEM IS ABOUT TO SHUTDOWN",timeout=10)
    os.system("shutdown /s /t 15")
    
def restart():
    notification.notify(message="YOUR SYSTEM IS ABOUT TO RESTART",timeout=10)
    os.system("shutdown /r /t 15")
    
for i in range(50):
    print("enter which one you want to select from following --->")
    print("(1)system shutdown")
    print("(2)system restart")
    print("(3)exit")
    x=input()
    if x=="1":
        shutdown()
        break
    elif x=="2":
        restart()
        break
    elif x=="3":
        break
    else:
        print("select from menu only------->")


