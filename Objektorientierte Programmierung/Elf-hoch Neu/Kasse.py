class Kasse(object):
    def __init__(self, pStartwert):
        self.stand = pStartwert

    def auszahlen(self):
        temp = self.stand
        self.stand = 0
        return temp

    def einzahlen(self, pBetrag):
        self.stand += pBetrag

    def getStand(self):
        return self.stand