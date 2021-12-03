class Spieler(object):
    def __init__(self, name):
        self.name = name
        self.coins = 0

    def addCoins(self, amount):
        self.coins += amount

    def removeCoins(self, amount):
        self.coins -= amount

        if(self.coins < 0):
            self.coins = 0

    def removeAllCoins(self):
        self.coins = 0