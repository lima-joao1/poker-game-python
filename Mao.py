
class Mao:
    def __init__(self):
        self.__cartas = []


    def receberCarta(self, carta):
        self.__cartas.append(carta)

    def getCartas(self):
        return self.__cartas
    
    def limpar(self):
        self.__cartas.clear()

    def mostrar(self):
        resultado = ""
        
        for i in range(len(self.__cartas)):
            resultado += str(self.__cartas[i])
            
            if i < len(self.__cartas) - 1:
                resultado += ", "

        return resultado