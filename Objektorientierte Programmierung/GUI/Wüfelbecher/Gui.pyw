import tkinter as tk
from tkinter import ttk
from tkinter import * 
from Würfel import *

würfel = Würfel()

def btnClickFunction():
    würfel.werfen()
    labelE1.config(text="Ergebnis: " + str(würfel.getAugen()))

    würfel.werfen()
    labelE2.config(text="Ergebnis: " + str(würfel.getAugen()))

    würfel.werfen()
    labelE3.config(text="Ergebnis: " + str(würfel.getAugen()))

    würfel.werfen()
    labelE4.config(text="Ergebnis: " + str(würfel.getAugen()))

    würfel.werfen()
    labelE5.config(text="Ergebnis: " + str(würfel.getAugen()))

root = Tk()

root.geometry('290x200')
root.configure(background='#F0F8FF')
root.title('Würfelbecher')

labelE1 = Label(root, text='E1', fg='#000', bg='#F0F8FF', font=('arial', 12, 'normal'))
labelE1.place(x=15, y=5)

labelE2 = Label(root, text='E2', fg='#000',bg='#F0F8FF', font=('arial', 12, 'normal'))
labelE2.place(x=15, y=25)

labelE3 = Label(root, text='E3', fg='#000',bg='#F0F8FF', font=('arial', 12, 'normal'))
labelE3.place(x=15, y=45)

labelE4 = Label(root, text='E4', fg='#000',bg='#F0F8FF', font=('arial', 12, 'normal'))
labelE4.place(x=15, y=65)

labelE5 = Label(root, text='E5', fg='#000',bg='#F0F8FF', font=('arial', 12, 'normal'))
labelE5.place(x=15, y=85)

Button(root, text='Werfen', fg='#000',bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=205, y=5)

root.mainloop()
