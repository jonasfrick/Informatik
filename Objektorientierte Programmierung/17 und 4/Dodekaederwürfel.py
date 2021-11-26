import random

class Dodekaederwuerfel(object):
    def __init__(self):
        self.augen = random.randint(1, 12)

    def werfen(self):
        self.augen = random.randint(1, 12)