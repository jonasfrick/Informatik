class Kasse(object):
    def __init__(self, pStartwert):
        self.stand = pStartwert

    def auszahlen(self, pBetrag):
         self.stand = self.stand - pBetrag

    def einzahlen(self, pBetrag):
        self.stand += pBetrag

    def getStand(self):
        return self.stand