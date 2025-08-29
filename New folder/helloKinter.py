from tkinter import *
root = Tk()
# #creating label widget
# #myLabel= Label(root,text="helloWorld!")
# myLabel1=Label(root,text=("helloWorld"))
# myLabel2=Label(root,text=("second line"))

# #packing it in screen
# #myLabel.pack()
# myLabel1.grid(row=0,column=0)
# myLabel2.grid(row=1,column=1)
def myClick():
    myLabel=Label(root,text="clicked a button",fg="blue",bg="white")
    myLabel.pack()
myButton=Button(root,text="clickMe",command=myClick,padx=50,pady=50,fg="blue").pack()

root.mainloop()