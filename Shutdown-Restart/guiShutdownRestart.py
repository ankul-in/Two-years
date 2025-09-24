#https://youtu.be/1wH0m8-Mkn4
from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restartwithtime():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")


st=Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="#FDF6EC")

r_button = Button(st,background="#FFB6B9",text="RESTART",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)


rt_button = Button(st,background="#FFB6B9",text="RESTART TIME",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="plus",command=restartwithtime)
rt_button.place(x=150,y=170,height=50,width=200)


lg_button = Button(st,background="#FFB6B9",text="LOG-OUT",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)


st_button = Button(st,background="#FFB6B9",text="SHUTDOWN",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)

st.mainloop()
