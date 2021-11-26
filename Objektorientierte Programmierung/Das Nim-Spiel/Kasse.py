class Kasse(object):
    def __init__(self, startWert):
        self.stand = startWert

    def ziehen(self, anzahl):
        self.stand -= anzahl

    def getStand(self):
        return self.stand