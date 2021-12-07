from tkinter import *

def addition():
	ergebnis = str(round(float(entryZahl1.get()) + float(entryZahl2.get()), 2))

	labelErgebisWert.config(text=ergebnis)

def subtraktion():
	ergebnis = str(round(float(entryZahl1.get()) - float(entryZahl2.get()), 2))

	labelErgebisWert.config(text=ergebnis)

def multiplikation():
	ergebnis = str(round(float(entryZahl1.get()) * float(entryZahl2.get()), 2))

	labelErgebisWert.config(text=ergebnis)

def division():
	ergebnis = str(round(float(entryZahl1.get()) / float(entryZahl2.get()), 2))

	labelErgebisWert.config(text=ergebnis)

tkFenster = Tk()
tkFenster.title('Taschenrechner')
tkFenster.geometry('258x195')

labelZahl1 = Label(master=tkFenster, bg='#FFCFC9', text='Zahl 1:')
labelZahl1.place(x=54, y=24, width=100, height=27)

entryZahl1 = Entry(master=tkFenster, bg='white')
entryZahl1.place(x=164, y=24, width=40, height=27)

labelZahl2 = Label(master=tkFenster, bg='#FFCFC9', text='Zahl 2:')
labelZahl2.place(x=54, y=64, width=100, height=27)

entryZahl2 = Entry(master=tkFenster, bg='white')
entryZahl2.place(x=164, y=64, width=40, height=27)

buttonAddition = Button(master=tkFenster, bg='#FBD975', text='+', command=addition)
buttonAddition.place(x=54, y=104, width=27, height=27)

buttonSubtraktion = Button(master=tkFenster, bg='#FBD975', text='-', command=subtraktion)
buttonSubtraktion.place(x=85, y=104, width=27, height=27)

buttonMultiplikation = Button(master=tkFenster, bg='#FBD975', text='*', command=multiplikation)
buttonMultiplikation.place(x=88 + 27, y=104, width=27, height=27)

buttonDivision = Button(master=tkFenster, bg='#FBD975', text='/', command=division)
buttonDivision.place(x=92 + 27 * 2, y=104, width=27, height=27)

labelErgebnis = Label(master=tkFenster, bg='#D5E88F', text='Ergebnis:')
labelErgebnis.place(x=54, y=144, width=100, height=27)

labelErgebisWert = Label(master=tkFenster, bg='gray', text='')
labelErgebisWert.place(x=164, y=144, width=40, height=27)

tkFenster.mainloop()