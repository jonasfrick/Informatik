from ZählerMitObergrenze import Zaehler

# Sekundenzähler

# Zähler definieren
zaehler = Zaehler(60)
#zaehler.grenze = 60 # Für Stunden auf 24 setzen <-- Auskommentieren, wenn die Obergrenze 60 sein soll

# Zufällige Schleife zum testen
for i in range(0, 100):

    # Stand ausgeben
    print("Stand:", zaehler.stand)

    # Zähler erhöhen
    zaehler.weiterZaehlen()