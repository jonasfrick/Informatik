from Spieler import *
from Würfel import *

class Spielmanager(object):
    __slots__ = ('rSpieler1', 'rSpieler2', 'rSpieler3', 'player')

    def __init__(self, pSpieler1, pSpieler2, pSpieler3):
        self.rSpieler1 = pSpieler1
        self.rSpieler2 = pSpieler2
        self.rSpieler3 = pSpieler3
        self.player = [self.rSpieler1, self.rSpieler2, self.rSpieler3]

    def spielrundeDurchfuehren(self):
        while len(self.player) > 1:
            for spieler in self.player:
                spieler.spielen()
                print(spieler.getName(), spieler.getMarken())

                if(spieler.getMarken() <= 0):
                    self.player.remove(spieler)
                    print(spieler.getName(), "hat verloren")

        print()
        print(self.player[0].getName(), "hat gewonnen")

