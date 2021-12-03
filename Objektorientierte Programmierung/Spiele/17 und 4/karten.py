from kartenstapel import Kartenstapel

def a():
    # Testprogramm
    kartenstapel = Kartenstapel()
    print(kartenstapel.kartenListe)
    print()
    kartenstapel.mischen()
    print(kartenstapel.kartenListe)
    print()
    print(kartenstapel.istLeer())
    gezogeneKarte = kartenstapel.karteZiehen()
    print(gezogeneKarte)
    print(kartenstapel.kartenListe)

def b():
    kartenstapel = Kartenstapel()
    kartenstapel.mischen()
    print("Stapel ist gemischt")
    print()

    while not kartenstapel.istLeer():
        gezogeneKarte = kartenstapel.karteZiehen()
        print(gezogeneKarte)

    print()
    print("Der Stapel ist leer!")

b()