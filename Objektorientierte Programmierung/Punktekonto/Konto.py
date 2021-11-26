class Konto(object):

    def __init__(self, name: str):
        self.__name = name
        self.punkte = 0

    def hinzufügen(self, anzahl: int):
        self.punkte += anzahl

    def entfernen(self, anzahl: int):
        self.punkte -= anzahl

        if (self.punkte < 0):
            self.punkte = 0