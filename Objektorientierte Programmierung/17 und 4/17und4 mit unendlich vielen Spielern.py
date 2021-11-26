# Spiel: 17 und 4

# Importieren der Klassen in Kartenspiel.py
from kartenspiel import *

kartenstapel = Kartenstapel()

playerX = int(input("Wie viele Spieler gibt es?: "))

for i in range(0, playerX):
    player = Kartenhaufen()
    playerInGame = True
    
    while (player.wert < 21) or (playerInGame):
        print()
        print("Willst du (Spieler " + str(i) + ") eine Karte ziehen?")
        print("Dein Wert liegt bei:", player.wert)
        x = input("Ja oder nein? ").lower()

        if(x == "ja"):
             # Karte ziehen
            karte = kartenstapel.karteZiehen()
            print("Karte:", karte)
            
            # Kartenwert dem Spieler hinzufügen
            player.hinzufuegen(karte)
            print("Dein Wert:", player.wert)
            print("")
        elif(x == "nein"):
            print("Spieler "+ str(i) + " ist ausgestiegen!")
            print("Der Wert des Spielers lag bei:", player.wert)
            print("")
            playerInGame = False

        # Wenn der Wert des Spielers über 21 ist, ist das Spiel verloren
        if(player.wert > 21):
            print()

            for j in range(0, 10):
                print("Du hast Verloren!")
            playerInGame = False
        elif(player.wert == 21):
            print()
            
            for j in range(0, 10):
                print("Du hast Gewonnen!")
            
            playerInGame = False

