# Spiel: 17 und 4

# Importieren der Klassen in Kartenspiel.py
from kartenspiel import *

kartenstapel = Kartenstapel()
spieler1 = Kartenhaufen()
spieler2 = Kartenhaufen()
kartenstapel.mischen()

# Variablen, um zu überprüfen, ob die Spieler noch nicht ausgestiegen sind
playerOneInGame = True
playerTwoInGame = True

# Solange die Werte von mindestens einem Spieler kleiner als 21 ist und mindestens ein Spieler im Spiel ist
while (spieler1.wert < 21 or spieler2.wert < 21) and (playerOneInGame or playerTwoInGame):
    # Abfragen, ob Spieler 1 noch nicht verloren hat
    if(playerOneInGame):
        print()
        print("Willst du (Spieler 1) eine Karte ziehen?")
        print("Deine Karten sind " + str(spieler1.wert) + " wert")

        # Eingabe abfragen
        x = input("Karte ziehen? (Ja oder Nein): ").lower()

        # Wenn Eingabe = 'Ja'
        if(x == "ja"):
            # Karte ziehen
            karte = kartenstapel.karteZiehen()
            print("Karte:", karte)
            
            # Kartenwert dem Spieler hinzufügen
            spieler1.hinzufuegen(karte)
            print("Dein Wert:", spieler1.wert)
            print("")

        # Wenn Eingabe = 'Nein'
        elif(x == "nein"):
            print("Spieler1 ist ausgestiegen!")
            print("Der Wert des Spielers lag bei:", spieler1.wert)
            print("")
            playerOneInGame = False

        # Wenn der Wert des Spielers über 21 ist, ist das Spiel verloren
        if(spieler1.wert > 21):
            print("Du hast Verloren!")
            playerOneInGame = False
        elif(spieler1.wert == 21):
            print()
            print("Du hast Gewonnen!")
            playerOneInGame = False

    if(playerTwoInGame):
        print()
        print("Willst du (Spieler 2) eine Karte ziehen?")
        print("Deine Karten sind " + str(spieler2.wert) + " wert")
        x = input("Karte ziehen? (Ja oder Nein): ").lower()

        if(x == "ja"):
            karte = kartenstapel.karteZiehen()
            print("Karte:", karte)
            spieler2.hinzufuegen(karte)
            print("Dein Wert:", spieler2.wert)
            print("")
        elif(x == "nein"):
            print("Spieler2 ist ausgestiegen!")
            print("Der Wert des Spielers lag bei:", spieler2.wert)
            print("")
            playerTwoInGame = False

        if(spieler2.wert > 21):
            print("Du hast Verloren!")
            playerTwoInGame = False
        elif(spieler2.wert == 21):
            print()
            print("Du hast Gewonnen!")
            playerTwoInGame = False

print("")
print("Das Spiel ist beendet!")