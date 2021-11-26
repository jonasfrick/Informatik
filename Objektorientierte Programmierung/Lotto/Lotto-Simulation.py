from Lottogeraet import Lottogeraet

dev = Lottogeraet()

guesses = []
winCounter = 0
win = 0
simulations = int(input("Wie viele Durchgänge sollen simuliert werden? \n"))

print("Gib die Zahlen nacheinander ein \n")
for i in range(0, 6):
    guesses.append(int(input("")))

print("Guesses: ", guesses) # DEBUG

for i in range(0, simulations):
    winCounter = 0
    dev.geraetVorbereiten()
    dev.ziehungDurchfuehren()

    for guess in guesses:
        if (guess in dev.getGezogeneKugeln()):
            winCounter += 1

    if (winCounter == 6):
        win += 1

    print("WinCounter:", winCounter, "Win", win, "Simulation", i)

print("Win", win)