from Würfel import Würfel
from Spieler import Spieler

# zufällige Namen
namen = ["Johnny", "Karsten", "Anton", "Marlon", "Kevin", "Marius", "Franz", "Heinrich", "Klaus", "KarateKidddd"]

# Liste aller Spieler
player = []

# Spielmarken in der Mitte
kasse = 0

print("[DEBUG] Programm wurde gestartet!")
print()

# Spielerliste leeren
player.clear()

# Für jeden Namen/Spieler einen Spieler anlegen
for name in namen:
    spieler = Spieler(name)
    player.append(spieler)
    print(spieler.name, "ist dem Spiel beigetreten")

print()

# Allen Spielern gleich viele Marken geben
for spieler in player:
    spieler.removeAllCoins()
    spieler.addCoins(40)
    print(spieler.name, "hat jetzt 40 Spielmarken")

# Solange noch mehr als ein Spieler noch Marken hat wird gespielt
while(len(player) > 1):
    # Für jeden Spieler
    for spieler in player:
        # Wenn der Spieler weniger als oder 0 Spielmarken hat scheidet er aus
        if(spieler.coins <= 0):
            player.remove(spieler) # Spieler entfernen
            print()
            print(spieler.name, "hat verloren") # Ausgabe wenn jemand verloren hat
            print()
            break

        # Würfel definineren
        würfel1 = Würfel()
        würfel2 = Würfel()

        # Würfel werfen
        würfel1.werfen()
        würfel2.werfen()
        result = würfel1.getAugen() + würfel2.getAugen() # Augenzahl beider Würfel zusammen rechnen

        # Verschiedene Würfelmöglichkeiten auswerten
        if(result == 11): # Wenn das Ergebnis 11 ist, bekommt der Spieler alle Spielmarken aus der Mitte
            spieler.addCoins(kasse)
            kasse = 0
        elif(result == 12): # Wenn das Ergebnis 12 ist, muss der Spieler 12 Marken in die Mitte legen
            spieler.removeCoins(12)
            kasse = kasse + 12
        elif (result < 11): # Wenn das Ergebnis kleiner als 11 ist, muss der Spieler die Differenz zwischen der Augenzahl und 11 in Spielmarken in die Mitte legen
            spieler.removeCoins(11 - result)
            kasse += 11 - result
        else: # DEBUG
            print("[DEBUG] ERROR")

        print(spieler.name, "hat eine", result, "gewürfelt. Er/Sie hat noch", spieler.coins, "übrig.") # Ausgabe der Würfelaugen und Anzahl der Spielmarken des Spielers

# Gewinner ausgeben
print()
print(player[0].name, "hat gewonnen!")
print()