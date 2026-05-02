class Carta:
    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit

    def getValue(self):
        return self.__value
    
    def getSuit(self):
        return self.__suit
    
    def __str__(self):
        return f"{self.__value} de {self.__suit}"