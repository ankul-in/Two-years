#https://youtu.be/CIm5vfsfgO0

# import tkinter as tk
# from PIL import Image,ImageTk
# import random

# window = tk.Tk()
# window.geometry("500x500")
# window.title("DiceRoll")


# dice=[r"D:\PY\dieRollSimulator\dice1.png",r"D:\PY\dieRollSimulator\dice2.png",r"D:\PY\dieRollSimulator\dice3.png",r"D:\PY\dieRollSimulator\dice4.png",r"D:\PY\dieRollSimulator\dice5.png",r"D:\PY\dieRollSimulator\dice6.png"]
# image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
# image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))

# label1=tk.Label(window,image=image1)
# label2=tk.Label(window,image=image2)

# label1.place(x=40, y=100)
# label2.place(x=300,y=100)

# def dice_roll():
#     image= ImageTk.PhotoImage(image.open(random.choice(dice)).resize((800, 600))
#     label1.configure(image=image1)
#     label1.image=image1

# button = tk.Button(window,text="roll",bg="green",fg="white",font="Times 20 bold",command=dice_roll)
# button.place(x=200,y=0)

# window.mainloop()


import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("450x300")
window.title("DiceRoll")

dice = [
    r"D:\PY\dieRollSimulator\dice1.png",
    r"D:\PY\dieRollSimulator\dice2.png",
    r"D:\PY\dieRollSimulator\dice3.png",
    r"D:\PY\dieRollSimulator\dice4.png",
    r"D:\PY\dieRollSimulator\dice5.png",
    r"D:\PY\dieRollSimulator\dice6.png"
]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((100, 100)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((100, 100)))

label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

label1.place(x=40, y=100)
label2.place(x=300, y=100)

def dice_roll():
    new_image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((100, 100)))
    new_image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((100, 100)))
    label1.configure(image=new_image1)
    label1.image = new_image1
    label2.configure(image=new_image2)
    label2.image = new_image2

button = tk.Button(window, text="Roll", bg="white", fg="black", font="Times 20 bold", command=dice_roll)
button.place(x=200, y=0)

window.mainloop()