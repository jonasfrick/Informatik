# Importieren der Klassen in Kartenspiel.py
from kartenspiel import *

over21 = 0

for i in range(0, 10000):
    kartenstapel = Kartenstapel()
    spieler = Kartenhaufen()
    kartenstapel.mischen()
    
    while (spieler.wert < 18):
        spieler.hinzufuegen(kartenstapel.karteZiehen())
        print("Wert:", spieler.wert)

        if (spieler.wert > 21):
            over21 += 1

print("Wie oft war der Spielerwert über 21? (aus 10000 Durchläufen)")
print(str(over21) + " Mal")