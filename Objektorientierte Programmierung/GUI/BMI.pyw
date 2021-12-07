from tkinter import *

def buttonBerechnenClick():
    # Übernahme der Daten
    gewicht = float(entryGewicht.get())
    groesse = float(entryGroesse.get())
    # Verarbeitung der Daten
    bmi = gewicht/(groesse*groesse)
    bmiAnzeige = str(round(bmi*10)/10)
    # Anzeige der Daten
    labelBMI.config(text=bmiAnzeige)

# Fenster
tkFenster = Tk()
tkFenster.title('BMI')
tkFenster.geometry('258x195')
# Label mit Aufschrift Gewicht
labelGewicht = Label(master=tkFenster, bg='#FFCFC9', text='Gewicht in kg:')
labelGewicht.place(x=54, y=24, width=100, height=27)
# Entry für das Gewicht
entryGewicht = Entry(master=tkFenster, bg='white')
entryGewicht.place(x=164, y=24, width=40, height=27)
# Label mit Aufschrift Größe
labelGroesse = Label(master=tkFenster, bg='#FFCFC9', text='Größe in m:')
labelGroesse.place(x=54, y=64, width=100, height=27)
# Entry für die Größe
entryGroesse = Entry(master=tkFenster, bg='white')
entryGroesse.place(x=164, y=64, width=40, height=27)
# Button zum Berechnen
buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='berechnen', command=buttonBerechnenClick)
buttonBerechnen.place(x=54, y=104, width=100, height=27)
# Label mit Aufschrift BMI-Wert
labelBMIWert = Label(master=tkFenster, bg='#D5E88F', text='BMI-Wert:')
labelBMIWert.place(x=54, y=144, width=100, height=27)
# Label für den BMI-Wert
labelBMI = Label(master=tkFenster, bg='gray', text='')
labelBMI.place(x=164, y=144, width=40, height=27)
# Aktivierung des Fensters
tkFenster.mainloop()