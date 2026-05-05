from Mao import Mao

class Player:
    def __init__(self):
        self.__playerMoney = 0
        self.__hand = Mao()

    def getMoney(self):
        return self.__playerMoney
    
    def addMoney(self, money):
        self.__playerMoney += money

    def getMao(self):
        return self.__hand