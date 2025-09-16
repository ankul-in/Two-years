#https://www.youtube.com/watch?v=RQi4FmBvN_k&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=10


from tkinter import *
import datetime

def date_time():
    time=datetime.datetime.now()
    hr = time.strftime("%I")
    mi = time.strftime("%M")
    sec= time.strftime("%S")
    am = time.strftime("%p")
    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%y")
    day = time.strftime("%a")




    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)

    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)


    lab_hr.after(200,date_time)


clock=Tk()
clock.title("    ****Digital Clock****")
clock.geometry("1000x500")
clock.config(bg="#F6F1E9")


#time
lab_hr=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_hr.place(x=120,y=45,height=110,width=100)
lab_hr_txt=Label(clock,text="Hour",font=("Time New Roman",20,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_hr_txt.place(x=120,y=190,height=40,width=100)

lab_min=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_min.place(x=340,y=45,height=110,width=100)
lab_min_txt=Label(clock,text="Min.",font=("Time New Roman",20,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_min_txt.place(x=340,y=190,height=40,width=100)

lab_sec=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_sec.place(x=560,y=45,height=110,width=100)
lab_sec_txt=Label(clock,text="Sec.",font=("Time New Roman",20,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_sec_txt.place(x=560,y=190,height=40,width=100)

lab_am=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_am.place(x=720,y=45,height=110,width=100)
lab_am_txt=Label(clock,text="AM/PM",font=("Time New Roman",20,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_am_txt.place(x=720,y=190,height=40,width=100)

#date
lab_date=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_date.place(x=120,y=270,height=110,width=100)
lab_date_txt=Label(clock,text="Date",font=("Time New Roman",20,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_date_txt.place(x=120,y=410,height=40,width=100)

lab_month=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_month.place(x=340,y=270,height=110,width=100)
lab_month_txt=Label(clock,text="Min.",font=("Time New Roman",20,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_month_txt.place(x=340,y=410,height=40,width=100)

lab_year=Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_txt=Label(clock,text="Sec.",font=("Time New Roman",20,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_year_txt.place(x=560,y=410,height=40,width=100)

lab_day=Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_day.place(x=720,y=270,height=110,width=100)
lab_day_txt=Label(clock,text="AM/PM",font=("Time New Roman",20,"bold"),bg="#FFD93D",fg="#FF9A00")
lab_day_txt.place(x=720,y=410,height=40,width=100)
date_time()

clock.mainloop()
