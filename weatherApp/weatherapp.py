#https://youtu.be/G-FBEDM7b3Y

from tkinter import *
from tkinter import ttk
import requests


def data_get():

    city_name="city"
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=heregoesyoureid").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"]-273.15))
    preassure_label1.config(text=data["main"]["preassure"])






win = Tk()
win.title("weather application")
win.geometry("500x600")
win.config(bg="blue")

name_label=Label(win,text="weather App",font=("Time New Roman",40,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

list_name= [
"Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
"Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
"Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
"Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
"Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
"Uttar Pradesh", "Uttarakhand", "West Bengal"
]
com = ttk.Combobox(win,text="Weather App",values=list_name,font=("Time New Roman",25,"bold"))
com.place(x=25,y=120,height=50,width=450)



w_label=Label(win,text="weather Climate",font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=200)
w_label1=Label(win,text="",font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=200)


wb_label=Label(win,text="weather discription",font=("Time New Roman",16))
wb_label.place(x=25,y=330,height=50,width=200)
wb_label1=Label(win,text="",font=("Time New Roman",16))
wb_label1.place(x=250,y=330,height=50,width=200)


temp_label=Label(win,text="Temperature",font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=200)
temp_label1=Label(win,text="",font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=200)

preassure_label=Label(win,text="preassure",font=("Time New Roman",20))
preassure_label.place(x=25,y=470,height=50,width=200)
preassure_label1=Label(win,text="",font=("Time New Roman",20))
preassure_label1.place(x=250,y=470,height=50,width=200)





done_button=Button(win,text="Done",font=("Time New Roman",25,"bold"),command=data_get())
done_button.place(x=200,y=190,height=50,width=100)


win.mainloop()

