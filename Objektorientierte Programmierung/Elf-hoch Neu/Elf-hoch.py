from Kasse import *
from Spieler import *
from Spielmanager import *
from Würfel import *

würfel1 = Wuerfel()                          
würfel2 = Wuerfel()
kasse = Kasse(0)
spieler1 = Spieler('Winner', würfel1, würfel2, kasse)
spieler2 = Spieler('Looser', würfel1, würfel2, kasse)
spieler3 = Spieler('Zitterhand', würfel1, würfel2, kasse)
spielManager = Spielmanager(spieler1, spieler2, spieler3)

spielManager.spielrundeDurchfuehren()