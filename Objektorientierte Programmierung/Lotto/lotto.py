"""
    Lotto-Simulation
"""

from Lottogeraet import Lottogeraet

gerat = Lottogeraet()

gerat.geraetVorbereiten()
gerat.kugelZiehen()

print("Es wurde ", gerat.getGezogeneKugeln(), " gezogen")
print("Es sind noch die Kugeln", gerat.getVorhandeneKugeln(), " vorhanden")

gerat.ziehungDurchfuehren()
print("Es wurde ", gerat.getGezogeneKugeln(), " gezogen")
