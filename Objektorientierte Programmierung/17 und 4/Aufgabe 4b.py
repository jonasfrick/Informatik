# Importieren der Klassen in Kartenspiel.py
from kartenspiel import *

kartenstapel = Kartenstapel()
spieler = Kartenhaufen()
kartenstapel.mischen()

# Solange der Wert des Spielers kleiner als 18 ist, zieht er eine Karte
while (spieler.wert < 18):
    # Spieler den Kartenwert zuschreiben
    spieler.hinzufuegen(kartenstapel.karteZiehen())

    # Wert ausgeben
    print("Wert:", spieler.wert)