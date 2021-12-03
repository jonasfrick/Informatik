class Spielfeld(object):
    def __init__(self, stand):
        self.stand = stand

    def getStand(self):
        return self.stand

    def ziehen(self, anzahl):
        self.stand -= anzahl