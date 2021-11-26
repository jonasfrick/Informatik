#-----------------------------------------------------------
# WÃ¼rfel
#-----------------------------------------------------------

from random import randint

class Wuerfel(object):

    def __init__(self):

        """
        Die Methode __init__ erzeugt ein Wuerfel-Objekt.
        Die Augenzahl wird dabei auf eine Zufallszahl aus
        dem Bereich 1..6 gesetzt.
        """

        self.augen = randint(1, 6)

    def werfen(self):

        """
        Die Methode werfen erzeugt eine neue Augenzahl
        als Zufallszahl aus dem Bereich 1..6.
        """
        
        self.augen = randint(1, 6)
