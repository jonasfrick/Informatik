class Zaehler(object):
    def __init__(self, grenze):
        self.stand = 0
        self.grenze = grenze

    def weiterZaehlen(self):
        if(self.stand == self.grenze):
            self.stand = 0

        self.stand += 1

    def nullSetzen(self):
        self.stand = 0