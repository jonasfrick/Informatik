import tkinter as tk
from tkinter import ttk
from tkinter import * 
from math import *

def btnClickFunction():
    print("Clicked")

    x1 = float(xA.get())
    x2 = float(xB.get())
    x3 = float(xC.get())

    try:
        disc = x2**2 - 4 * x1 * x3

        e1 = (-x2 - sqrt(disc)) / (2 * x1)
        e2 = (-x2 + sqrt(disc)) / (2 * x1)

        labelX1.config(text="x1 = " + str(round(e1, 2)))
        labelX2.config(text="x2 = " + str(round(e2, 2)))
    except:
        labelX1.config(text="Keine Lösung")
        labelX2.config(text="")

root = Tk()

root.geometry('380x150')
root.configure(background='#F0F8FF')
root.title('Quadratgleichung lösen')

xA=Entry(root)
xA.place(x=20, y=33, width=40, height=26)

Label(root, text='x ^2 +', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=62, y=33)

xB=Entry(root)
xB.place(x=110, y=33, width=40, height=26)

Label(root, text='x +', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=152, y=33)

xC=Entry(root)
xC.place(x=180, y=33, width=40, height=26)

Label(root, text='= 0', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=222, y=33)
Label(root, text='Ergebnis:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=22, y=83)

labelX1 = Label(root, text='x1 = ', bg='#F0F8FF', font=('arial', 12, 'normal'))
labelX1.place(x=122, y=83)

labelX2 = Label(root, text='x2 = ', bg='#F0F8FF', font=('arial', 12, 'normal'))
labelX2.place(x=122, y=113)

Button(root, text='Berechnen', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=272, y=30)


root.mainloop()
