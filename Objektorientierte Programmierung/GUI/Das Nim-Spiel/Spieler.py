from random import randint

class Spieler(object):
    def __init__(self, name, spielfeld):
        self.name = name
        self.spielfeld = spielfeld

    def getName(self):
        return self.name

    def spielen(self):
        self.spielfeld.ziehen(randint(1, 3))