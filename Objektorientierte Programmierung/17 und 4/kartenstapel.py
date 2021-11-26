#-----------------------------------------------------------
# Kartenstapel
#-----------------------------------------------------------

from random import randint

class Kartenstapel(object):
    def __init__(self):

        """
        Die Methode __init__ erzeugt ein Kartenstapel-Objekt.
        Die 32 Karten werden hier in einer festen Reihenfolge
        in kodierter Form vorgegeben:
        'X-A' (Kreuz Ass), ..., 'K-7' (Karo 7)
        """

        self.kartenListe = [
            'X-A', 'X-K', 'X-D', 'X-B', 'X-10', 'X-9', 'X-8', 'X-7',
            'P-A', 'P-K', 'P-D', 'P-B', 'P-10', 'P-9', 'P-8', 'P-7',
            'H-A', 'H-K', 'H-D', 'H-B', 'H-10', 'H-9', 'H-8', 'H-7',
            'K-A', 'K-K', 'K-D', 'K-B', 'K-10', 'K-9', 'K-8', 'K-7'
            ]

    def mischen(self):

        """
        Die aktuell im Kartenstapel vorliegenden Karten werden neu angeordnet.
        Hierzu wird eine zufÃ¤llig gewÃ¤hlte neue Reihenfolge bestimmt.
        """

        neueListe = []
        aktuelleAnzahl = len(self.kartenListe)
        while aktuelleAnzahl > 0:
            i = randint(0, aktuelleAnzahl-1)
            neueListe = neueListe + [self.kartenListe[i]]
            del self.kartenListe[i]
            aktuelleAnzahl = len(self.kartenListe)
        self.kartenListe = neueListe

    def istLeer(self):

        """
        Die Methode liefert als Ergebnis True / False,
        falls der Kartenstapel leer / nicht leer ist.
        """

        if len(self.kartenListe) > 0:
            ergebnis = False
        else:
            ergebnis = True
        return ergebnis

    def karteZiehen(self):

        """
        Die oberste (erste) Karte des Kartenstapel wird aus
        dem Kartenstapel entfernt und als Ergebnis zurÃ¼ckgegeben
        Ist der Kartenstapel leer, wird keine Karte gezogen
        und der wert None zurÃ¼ckgegeben.
        """

        if len(self.kartenListe) > 0:
            gezogeneKarte = self.kartenListe[0]
            self.kartenListe = self.kartenListe[1:]
        else:
            gezogeneKarte = None
        return gezogeneKarte