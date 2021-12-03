from elf_hoch_classes import *

# Einstellungen
print("----------- Elf-Hoch -----------")
print()
spielerA = int(input("Anzahl der Spieler: "))
while not spielerA >= 2:
    print("FEHLER! Es werden mindestens zwei Spieler benötigt.")
    spielerA = int(input("Erneut angeben: "))

# Objekte generieren
w1 = Wuerfel()
w2 = Wuerfel()
kasse = Kasse()
spielerL = []
for i in range(spielerA):
    print()
    print("Spieler",i+1)
    name = str(input("Name: "))
    spielerL.append(Spieler(name,40,w1,w2,kasse))
GM = GameManager(spielerL)

# Hauptspiel
print()
print("--------------------------------")
print()
print("Jeder Spieler erhält zu Beginn 40 Marken")
print("Derjenige, der zuletzt noch welche übrig hat, gewinnt!")
print("Drücken Sie 'Enter', um eine Runde zu simulieren")
while GM.getSpielerA() > 1:
    e = input()
    GM.rundeSpielen()
print()
GM.Gewinner()

