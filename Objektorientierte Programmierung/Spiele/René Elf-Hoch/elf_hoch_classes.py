#-----------------------------------------------------------
# Würfel
#-----------------------------------------------------------

from random import randint

class Wuerfel(object):

    __slots__ = ('augen')

    def __init__(self):
        self.augen = randint(1, 6)

    def werfen(self):
        self.augen = randint(1, 6)
        #print(self.augen)

    def getAugen(self):
        return self.augen

#-----------------------------------------------------------
# Kasse
#-----------------------------------------------------------

class Kasse(object):

    __slots__ = ('stand')

    def __init__(self, pStartwert):
        self.stand = pStartwert

    def auszahlen(self, pBetrag):
        self.stand = self.stand - pBetrag

    def einzahlen(self, pBetrag):
        self.stand = self.stand + pBetrag

    def getStand(self):
        return self.stand

#-----------------------------------------------------------
# Spieler
#-----------------------------------------------------------

class Spieler(object):

    __slots__ = ('name', 'rMeineKasse', 'rWuerfel1', 'rWuerfel2', 'rSpielKasse')

    def __init__(self, pName, pMarken, pWuerfel1, pWuerfel2, pSpielKasse):
        self.name = pName
        self.rMeineKasse = Kasse(pMarken)
        self.rWuerfel1 = pWuerfel1
        self.rWuerfel2 = pWuerfel2
        self.rSpielKasse = pSpielKasse

    def spielen(self):
        self.rWuerfel1.werfen()
        self.rWuerfel2.werfen()
        augenGesamt = self.rWuerfel1.getAugen() + self.rWuerfel2.getAugen()

        print("Spieler", self.name, self.getMarken())

        if augenGesamt == 12:
            self.rMeineKasse.auszahlen(12)
            self.rSpielKasse.einzahlen(12)
        elif augenGesamt == 11:
            anzahlMarken = self.rSpielKasse.getStand()
            self.rSpielKasse.auszahlen(anzahlMarken)
            self.rMeineKasse.einzahlen(anzahlMarken)
        else:
            differenzBetrag = 11 - augenGesamt
            self.rMeineKasse.auszahlen(differenzBetrag)
            self.rSpielKasse.einzahlen(differenzBetrag)

    def getName(self):
        return self.name

    def getMarken(self):
        return self.rMeineKasse.getStand()


#-----------------------------------------------------------
# Spielmanager
#-----------------------------------------------------------

class Spielmanager(object):
    def __init__(self, pPlayer):
        self.pPlayer = pPlayer;

    def rundeSpielen(self):
        for i in self.pPlayer:
            i.spielen()

            if(i.getMarken() <= 0):
                self.pPlayer.remove(i)


    def getSpielerListe(self):
        return self.pPlayer