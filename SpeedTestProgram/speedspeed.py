#https://youtu.be/QdFOoagnBP4?si=I-h7lI_TSUP5O7o3

from tkinter import *
import speedtest

def speedcheck():
    try:
        sp = speedtest.Speedtest(secure=True)
        sp.get_servers()
        down = str(round(sp.download()/(10**6),3))+" Mbps"
        up = str(round(sp.upload()/(10**6),3))+" Mbps"
        lab_2.config(text=down)
        lab_3.config(text=up)
    except Exception as e:
        lab_2.config(text="Error")
        lab_3.config(text="Check Connection")


    
    

sp=Tk()
sp.title("SPEED-TEST")
sp.geometry("500x600")
sp.config(bg="#FFE775")
lab_1 = Label(sp,text="Internet Speed Test",font=("Time New roman",30,"bold"),bg="#FFE775",fg="#FC993C")
lab_1.place(x=60,y=40,height=50,width=380)
lab_down = Label(sp,text="Download Speed",font=("Time New roman",30,"bold"),bg="#FFE775",fg="#FC993C")
lab_down.place(x=60,y=130,height=50,width=380)
lab_2 = Label(sp,text="00",font=("Time New roman",30,"bold"),bg="#FFE775",fg="#FC993C")
lab_2.place(x=60,y=200,height=50,width=380)
lab_up = Label(sp,text="Upload Speed",font=("Time New roman",30,"bold"),bg="#FFE775",fg="#FC993C")
lab_up.place(x=60,y=290,height=50,width=380)
lab_3 = Label(sp,text="00",font=("Time New roman",30,"bold"),bg="#FFE775",fg="#FC993C")
lab_3.place(x=60,y=360,height=50,width=380)
button = Button(sp,text="Check Speed",font=("Time New roman",30,"bold"),bg="#8C2057",fg="#FC993C",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)


sp.mainloop()