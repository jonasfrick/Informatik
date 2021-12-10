from random import randint

class Würfel(object):

    def __init__(self):
        self.__augen__ = randint(1, 6)

    def werfen(self):
        self.__augen__ = randint(1, 6)

    def getAugen(self):
        return self.__augen__