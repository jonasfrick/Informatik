from Kasse import *
from Spieler import *
from Spielmanager import *
from Würfel import *

w1 = Wuerfel()                          
w2 = Wuerfel()
k = Kasse(0)
sp1 = Spieler('Winner', w1, w2, k)
sp2 = Spieler('Looser', w1, w2, k)
sp3 = Spieler('Zitterhand', w1, w2, k)
m = Spielmanager(sp1, sp2, sp3)

m.spielrundeDurchfuehren()
print(sp1.getMarken(), sp2.getMarken(), sp3.getMarken())