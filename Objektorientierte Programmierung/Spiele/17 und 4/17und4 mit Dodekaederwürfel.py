# Spiel: 17 und 4

# Importieren der Klassen in Dodekaederwürfel.py
from Dodekaederwürfel import Dodekaederwuerfel

wuerfel = Dodekaederwuerfel()
spieler1 = 0
spieler2 = 0

# Variablen, um zu überprüfen, ob die Spieler noch nicht ausgestiegen sind
playerOneInGame = True
playerTwoInGame = True

# Solange die Werte von mindestens einem Spieler kleiner als 21 ist und mindestens ein Spieler im Spiel ist
while (spieler1 < 21 or spieler2 < 21) and (playerOneInGame or playerTwoInGame):
    # Abfragen, ob Spieler 1 noch nicht verloren hat
    if(playerOneInGame):
        print()
        print("Willst du (Spieler 1) den Würfel werfen?")
        print("Deine Würfe sind " + str(spieler1) + " wert")

        # Eingabe abfragen
        x = input("Würfel werfen? (Ja oder Nein): ").lower()

        # Wenn Eingabe = 'Ja'
        if(x == "ja"):
            # Würfel werfen
            wuerfel.werfen()
            augen = wuerfel.augen
            print("Augen:", augen)
            
            # Augenwert dem Spieler hinzufügen
            spieler1 += augen
            print("Dein Wert:", spieler1)
            print("")

        # Wenn Eingabe = 'Nein'
        elif(x == "nein"):
            print("Spieler1 ist ausgestiegen!")
            print("Der Wert des Spielers lag bei:", spieler1)
            print("")
            playerOneInGame = False

        # Wenn der Wert des Spielers über 21 ist, ist das Spiel verloren
        if(spieler1 > 21):
            print("Du hast Verloren!")
            print("Du hast Verloren!")
            print("Du hast Verloren!")
            print("Du hast Verloren!")
            playerOneInGame = False
        elif(spieler1 == 21):
            print()
            print("Du hast Gewonnen!")
            print("Du hast Gewonnen!")
            print("Du hast Gewonnen!")
            print("Du hast Gewonnen!")
            playerOneInGame = False

    if(playerTwoInGame):
        print()
        print("Willst du (Spieler 2) den Würfel werfen?")
        print("Deine Würfe sind " + str(spieler2) + " wert")
        x = input("Würfel werfen? (Ja oder Nein): ").lower()

        if(x == "ja"):
            wuerfel.werfen()
            augen = wuerfel.augen
            print("Karte:", augen)
            spieler2 += augen
            print("Dein Wert:", spieler2)
            print("")
        elif(x == "nein"):
            print("Spieler2 ist ausgestiegen!")
            print("Der Wert des Spielers lag bei:", spieler2)
            print("")
            playerTwoInGame = False

        if(spieler2 > 21):
            print("Du hast Verloren!")
            print("Du hast Verloren!")
            print("Du hast Verloren!")
            print("Du hast Verloren!")
            playerTwoInGame = False
        elif(spieler2 == 21):
            print()
            print("Du hast Gewonnen!")
            print("Du hast Gewonnen!")
            print("Du hast Gewonnen!")
            print("Du hast Gewonnen!")
            playerTwoInGame = False

print("")
print("Das Spiel ist beendet!")