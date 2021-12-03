from random import randint

#--------------------------------------------------------------------------
# Würfel
#--------------------------------------------------------------------------

class Wuerfel(object):
    
    __slots__ = ('augen')

    def __init__(self):
        self.augen = randint(1, 6)

    def werfen(self):
        self.augen = randint(1, 6)
    
    def getAugen(self):
        return self.augen

#--------------------------------------------------------------------------
# Kasse
#--------------------------------------------------------------------------

class Kasse(object):
    
    __slots__ = ('stand')
    
    def __init__(self):
        self.stand = 0
    
    def einzahlen(self, betrag):
        self.stand += betrag
    
    def leeren(self):
        self.stand = 0
    
    def getStand(self):
        return self.stand

#--------------------------------------------------------------------------
# Spieler
#--------------------------------------------------------------------------

class Spieler(object):
    
    __slots__ = ('name','marken','rWuerfel1','rWuerfel2','rKasse','augen','abzug')
    
    def __init__(self, pName, pMarken, pWuerfel1, pWuerfel2, pKasse):
        self.name = pName
        self.marken = pMarken
        self.rWuerfel1 = pWuerfel1
        self.rWuerfel2 = pWuerfel2
        self.rKasse = pKasse
    
    def spielen(self):
        self.rWuerfel1.werfen()
        self.rWuerfel2.werfen()
        self.augen = self.rWuerfel1.getAugen() + self.rWuerfel2.getAugen()
        if self.augen == 11:
            self.marken += self.rKasse.getStand()
            self.rKasse.leeren()
        else:
            self.abzug = self.augen
            if self.augen != 12:
                self.abzug = 11 - self.augen
            if self.abzug > self.marken:
                self.abzug = self.marken
            self.marken -= self.abzug
            self.rKasse.einzahlen(self.abzug)
    
    def getName(self):
        return self.name
    
    def getMarken(self):
        return self.marken
    
    def getAugen(self):
        return self.augen
    
    def getAbzug(self):
        return self.abzug

#--------------------------------------------------------------------------
# Game Manager
#--------------------------------------------------------------------------

class GameManager(object):
    
    __slots__ = ('rSpielerL','rSpielerA')
    
    def __init__(self, pSpielerL):
        self.rSpielerL = pSpielerL
        self.rSpielerA = list(range(len(pSpielerL)))
    
    def rundeSpielen(self):
        print()
        for i in range(len(self.rSpielerL)):
            if (i in self.rSpielerA) and (len(self.rSpielerA) > 1):
                self.rSpielerL[i].spielen()
                print("  ",self.rSpielerL[i].getName(),"würfelt: ",self.rSpielerL[i].getAugen())
                print("------------------------------")
                if self.rSpielerL[i].getAugen() == 11:
                    print("JACKPOT!! Kasse wird geleert!")
                else:
                    print("Abzugebene Marken: ",self.rSpielerL[i].getAbzug())
                print("Markenstand:       ",self.rSpielerL[i].getMarken())
                if self.rSpielerL[i].getMarken() == 0:
                    print("  ",self.rSpielerL[i].getName(),"ist raus!")
                    self.rSpielerA.remove(i)
                print()
    
    def Gewinner(self):
        print("------ Sieger/-in:",self.rSpielerL[self.rSpielerA[0]].getName(),"------")
    
    def getSpielerA(self):
        return len(self.rSpielerA)

