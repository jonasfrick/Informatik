from tkinter import *

win = Tk()
win.title("Sebastian ist ein Stinker")
win.geometry("200x50")

label = Label(master=win, text="Sebastian", fg="white", bg="red", font=("Arial", 20))
label.place(x=0, y=0, width=200, height=20)

label = Label(master=win, text="du stinkst", fg="black", bg="red", font=("Arial", 15))
label.place(x=0, y=20, width=200, height=20)

win.mainloop()