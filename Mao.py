from abc import ABC, abstractmethod

class Mao:
    def __init__(self):
        self.__cartas = []


    def receberCarta(self, carta):
        self.__cartas.append(carta)

    def getCartas(self):
        return self.__cartas
    
    def limpar(self):
        self.__cartas.clear()