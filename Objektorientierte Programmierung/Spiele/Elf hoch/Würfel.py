from random import randint

class Würfel(object):
    def __init__(self):
        self._augen = randint(1, 6)

    def werfen(self):
        self._augen = randint(1, 6)

    def getAugen(self):
        return self._augen