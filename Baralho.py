from Carta import Carta
import random

class Baralho:
    def __init__(self):
        self.__cartas = []
        suits = ["Ouro", "Copas", "Paus", "Espadas"]
        values = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        
        for suit in suits:
            for value in values:
                carta = Carta(value, suit)
                self.__cartas.append(carta)
    
    def getCartas(self):
        return self.__cartas
    
    def embaralhar(self):
        random.shuffle(self.__cartas)

    def distribuir(self):
        return self.__cartas.pop(0)