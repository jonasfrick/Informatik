from Würfel import *
from Kasse import *

class Spieler(object):
    def __init__(self, name, wuerfel1, wuerfel2, kasse):
        self.name = name
        self.marken = 80
        self.rWuerfel1 = wuerfel1
        self.rWuerfel2 = wuerfel2
        self.rKasse = kasse

    def spielen(self):
        self.rWuerfel1.werfen()
        self.rWuerfel2.werfen()
        augenGesamt = self.rWuerfel1.getAugen() + self.rWuerfel2.getAugen()
        if augenGesamt == 12:
            self.marken = self.marken - 12
            self.rKasse.einzahlen(12)
        elif augenGesamt == 11:
            anzahlMarken = self.rKasse.getStand()
            self.rKasse.auszahlen(anzahlMarken)
            self.marken = self.marken + anzahlMarken
        else:
            differenzBetrag = 11 - augenGesamt
            self.marken = self.marken - differenzBetrag
            self.rKasse.einzahlen(differenzBetrag)

    def getName(self):
        return self.name

    def getMarken(self):
        return self.marken