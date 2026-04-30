from abc import ABC, abstractmethod

class Mao:
    def __init__(self):
        self.__minhasCartas = []


    @abstractmethod
    def extraiValor(self, outra):
        pass

    def showValue(self, value):
        values_to_combinations = { 
        }