from random import randint

class Wuerfel(object):
    def __init__(self):
        self.augen = randint(1, 6)
        self.wert = 0

    def werfen(self):
        self.augen = randint(1, 12)

    def getAugen(self):
        return self.augen