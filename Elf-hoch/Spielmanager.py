from Spieler import *
from Würfel import *

class Spielmanager(object):
    __slots__ = ('rSpieler1', 'rSpieler2', 'rSpieler3')

    def __init__(self, pSpieler1, pSpieler2, pSpieler3):
        self.rSpieler1 = pSpieler1
        self.rSpieler2 = pSpieler2
        self.rSpieler3 = pSpieler3

    def spielrundeDurchfuehren():
        print("Start")