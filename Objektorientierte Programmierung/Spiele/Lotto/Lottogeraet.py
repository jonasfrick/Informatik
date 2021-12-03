from random import randint

class Lottogeraet(object):
    def __init__(self):
        """
        erzeugt ein Objekt zur Simulation eines Lottogeraets
        """
        
        self.geraetVorbereiten()
        
        
    def geraetVorbereiten(self):
        """
        fuellt das Lottogeraet mit Kugeln von 1..49
        leert den Behaelter der gezogenen Kugeln
        """
        
        self.vorhandeneKugeln = list(range(1, 50))
        self.gezogeneKugeln = []

    def kugelZiehen(self):
        """
        zieht eine Kugel aus den noch vorhandenen Kugeln
        entfernt diese Kugel aus dem Kugelbehaelter
        legt die Kugel im Behaelter der gezogenen Kugeln ab
        """
        
        kugel = randint(1, 49)
        while not kugel in self.vorhandeneKugeln:
            kugel = randint(1, 49)
        i = self.vorhandeneKugeln.index(kugel)
        del self.vorhandeneKugeln[i]
        self.gezogeneKugeln = self.gezogeneKugeln + [kugel]

    def ziehungDurchfuehren(self):
        """
        zieht 6 Kugeln ohne Zuruecklegen
        legt alle Kugeln im Behaelter der gezogenen Kugeln ab
        """
        
        for i in range(6):
            self.kugelZiehen()

    def getVorhandeneKugeln(self):
        """
        liefert die noch vorhandenen Kugeln
        """
        
        return self.vorhandeneKugeln

    def getGezogeneKugeln(self):
        """
        liefert die gezogenen Kugeln
        """
        
        return self.gezogeneKugeln
