class SpielManager(object):
    def __init__(self, spielfeld, spielerliste):
        self.spielfeld = spielfeld
        self.spielerliste = spielerliste

    def spielen(self):
        for i in self.spielerliste:
            i.spielen()

            if(self.spielfeld.getStand() <= 0):
                self.spielerliste.remove(i)
                print(i.getName(), "hat verloren")

            print(str(self.spielfeld.getStand()))