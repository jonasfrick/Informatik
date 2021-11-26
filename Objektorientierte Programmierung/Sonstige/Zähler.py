class Zaehler(object):
    def __init__(self):
        self.stand = 0
        
    def weiterZaehlen(self):
        self.stand += 1

    def nullSetzen(self):
        self.stand = 0