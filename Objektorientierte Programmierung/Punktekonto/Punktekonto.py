from Konto import Konto

namen = ["Fridolin", "Kai-Uwe", "Ragnar", "Emil", "Richard", "Frank", "Mareike", "Mähdrescher", "Helikopter", "Marvin", "Carbonara"]

menschen = {}

for name in namen:
    konto = Konto(name)

    menschen[name] = konto

while True:
    for name, konto in menschen.items():
        req = int(input("Möchtest du \033[1m" + name + "\033[0m Punkte hinzufügen oder abziehen? (1 = hinzufügen, 2 = abziehen) \n"))

        if (req == 1):
            points = int(input("Wie viele Punkte möchtest du \033[1m" + name + "\033[0m hinzufügen? \n"))

            konto.hinzufügen(points)

            print("\033[1m" + name + "\033[0m hat jetzt " + str(konto.punkte) + " Punkte!")

        elif (req == 2):
            points = int(input("Wie viele Punkte möchtest du \033[1m" + name + "\033[0m abziehen? \n"))

            konto.entfernen(points)

            print("\033[1m" + name + "\033[0m hat jetzt " + str(konto.punkte) + " Punkte!")

        else:
            print("Das ist keine erlaubte Eingabe, du Spinner")