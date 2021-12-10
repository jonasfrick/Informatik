import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is the function called when the button is clicked
def btnClickFunction():
	label.config(text="Du stinkst.")



root = Tk()

# This is the section of code which creates the main window
root.geometry('770x490')
root.configure(background='#8A2BE2')
root.title('Hello, I\'m the main window')


# This is the section of code which creates the a label
label = Label(root, text='Ich bin toll', bg='#8A2BE2', font=('verdana', 50, 'bold'))
label.place(x=9, y=11)


# This is the section of code which creates a button
Button(root, text='Klick mich an', bg='#00008B', font=('verdana', 20, 'normal'), command=btnClickFunction).place(x=439, y=11)


root.mainloop()
