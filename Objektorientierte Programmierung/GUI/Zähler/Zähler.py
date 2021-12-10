class Zähler(object):
    def __init__(self):
        self.stand = 0

    def weiterZählen(self):
        self.stand += 1

    def nullSetzen(self):
        self.stand = 0

    def zurückZählen(self):
        if(self.stand > 0):
            self.stand -= 1

    def getStand(self):
        return self.stand

    def setStand(self, stand):
        self.stand = stand