class Zähler(object):
    def __init__(self):
        self.__stand__ = 0

    def weiterZählen(self):
        self.__stand__ += 1

    def nullSetzen(self):
        self.__stand__ = 0

    def zurückZählen(self):
        if(self.__stand__ > 0):
            self.__stand__ -= 1

    def getStand(self):
        return self.__stand__

    def setStand(self, stand):
        self.__stand__ = stand