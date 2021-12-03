from tkinter import *
# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Kalender')
tkFenster.geometry('130x165')
# Label für die Anzeige der Daten
labelMonat = Label(master=tkFenster, text='Dezember', fg='#2980b9', font=('Comic Sans MS', 16))
labelMonat.place(x=5, y=5, width=120, height=20)
labelTag = Label(master=tkFenster, text='03', fg='#3498db', font=('Comic Sans MS', 72))
labelTag.place(x=5, y=30, width=120, height=100)
labelWochentag = Label(master=tkFenster, text='Freitag',font=("Comic Sans MS", 10))
labelWochentag.place(x=35, y=135, width=60, height=30)
# Aktivierung des Fensters
tkFenster.mainloop()