from Spielmanager import *
from Spielfeld import *
from Spieler import *

spielFeld = Spielfeld(20)
spielerListe = [Spieler("Spieler", spielFeld), Spieler("Computer", spielFeld)]
spielManager = SpielManager(spielFeld, spielerListe)

while len(spielManager.spielerliste) > 1:
    spielManager.spielen()
