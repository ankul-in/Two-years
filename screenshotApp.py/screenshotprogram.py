#https://youtu.be/QaC9PUMbjF4

import pyautogui
from tkinter import *


def takeSS():
    
    addData = entry.get()
    
    ss=pyautogui.screenshot()
    ss.save(f"D:/PY/screenshotApp.py/{addData}.png")

win=Tk()


win.title("ss program")
win.geometry("500x500")
win.config(bg="#FFECC0")
win.resizable(False,False)


entry = Entry(win,font=("Time New Roman" , 30))
entry.place(x=10,height=70,width=460,y=50)

button=Button(win,text="Take-SS", font=( "Time New Roman",40,"bold"),command=takeSS)
button.place(x=100,y=200,height=100,width=300)



win.mainloop()



# ss=pyautogui.screenshot()
# ss.save(r"screenshotApp.py/test1.png")