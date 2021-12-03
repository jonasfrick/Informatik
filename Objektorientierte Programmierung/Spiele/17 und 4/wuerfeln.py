from Dodekaederwürfel import Dodekaederwuerfel

# Würfel erstellen
w1 = Dodekaederwuerfel()
w2 = Dodekaederwuerfel()
w3 = Dodekaederwuerfel()

print("----")

# Würfel 1 werfen bis er eine 12 zeigt
while w1.augen != 12:
    w1.werfen()
    print("Würfel 1:", w1.augen)

print("----")

# Würfel 2 werfen bis er eine 12 zeigt
while w2.augen != 12:
    w2.werfen()
    print("Würfel 2:", w2.augen)

print("----")

# Würfel 3 werfen bis er eine 12 zeigt
while w3.augen != 12:
    w3.werfen()
    print("Würfel 3:", w3.augen)

print("Alle Würfel zeigen 6 Augen!")
print(w1.augen)
print(w2.augen)
print(w3.augen)