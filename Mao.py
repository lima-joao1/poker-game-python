from abc import ABC, abstractmethod
from collections import Counter
from itertools import combinations


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
    
    ORDEM_VALORES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Ás"]

    RANKING_MAOS = [
        "Carta Alta",
        "Um Par",
        "Dois Pares",
        "Trinca",
        "Straight",
        "Flush",
        "Full House",
        "Quadra",
        "Straight Flush",
        "Royal Flush",
    ]

    @staticmethod
    def _get_valores_numericos(cartas):
        return sorted(
            [Mao.ORDEM_VALORES.index(c.getValue()) for c in cartas]
        )

    @staticmethod
    def _get_naipes(cartas):
        return [c.getSuit() for c in cartas]

    @staticmethod
    def _is_flush(cartas):
        return len(set(Mao._get_naipes(cartas))) == 1

    @staticmethod
    def _is_straight(cartas):
        valores = Mao._get_valores_numericos(cartas)
        if valores == list(range(valores[0], valores[0] + 5)):
            return True
        # Sequência especial: A-2-3-4-5
        if sorted(valores) == [0, 1, 2, 3, 12]:
            return True
        return False

    @staticmethod
    def _is_royal(cartas):
        valores = set(Mao._get_valores_numericos(cartas))
        return valores == {8, 9, 10, 11, 12} 

    @staticmethod
    def _avaliar_cinco(cartas):
        contagens   = Counter(c.getValue() for c in cartas)
        frequencias = sorted(contagens.values(), reverse=True)

        flush    = Mao._is_flush(cartas)
        straight = Mao._is_straight(cartas)
        royal    = Mao._is_royal(cartas)

        if royal and flush:               
            return "Royal Flush"
        if straight and flush:            
            return "Straight Flush"
        if frequencias[0] == 4:           
            return "Quadra"
        if frequencias[:2] == [3, 2]:     
            return "Full House"
        if flush:                         
            return "Flush"
        if straight:                      
            return "Straight"
        if frequencias[0] == 3:           
            return "Trinca"
        if frequencias[:2] == [2, 2]:     
            return "Dois Pares"
        if frequencias[0] == 2:           
            return "Um Par"
        else:
            return "Carta Alta"

    @staticmethod
    def avaliar(cartas):
        total = len(cartas)

        if total < 2:
            return "Cartas insuficientes"

        if total == 2:
            contagens = Counter(c.getValue() for c in cartas)
            if max(contagens.values()) == 2:
                return "Um Par"
            naipes = Mao._get_naipes(cartas)
            valores = Mao._get_valores_numericos(cartas)
            if len(set(naipes)) == 1:
                return "Suited (mesmo naipe)"
            if abs(valores[0] - valores[1]) == 1:
                return "Conectadas (sequência potencial)"
            else:
                return "Carta Alta"

        if total in (3, 4):
            contagens   = Counter(c.getValue() for c in cartas)
            frequencias = sorted(contagens.values(), reverse=True)
            if frequencias[0] == 4:           
                return "Quadra"
            if frequencias[0] == 3:           
                return "Trinca"
            if frequencias[:2] == [2, 2]:     
                return "Dois Pares"
            if frequencias[0] == 2:           
                return "Um Par"
            else:
                return "Carta Alta"

        melhor_rank = -1
        melhor_mao  = "Carta Alta"

        for combo in combinations(cartas, 5):
            nome = Mao._avaliar_cinco(list(combo))
            rank = Mao.RANKING_MAOS.index(nome)
            if rank > melhor_rank:
                melhor_rank = rank
                melhor_mao  = nome

        return melhor_mao
    
    @staticmethod
    def desempate(cartas_player, cartas_enemy):
        
        valores_player = sorted(
            [Mao.ORDEM_VALORES.index(c.getValue()) for c in cartas_player],
            reverse=True
        )
        valores_enemy = sorted(
            [Mao.ORDEM_VALORES.index(c.getValue()) for c in cartas_enemy],
            reverse=True
        )

        for v_player, v_enemy in zip(valores_player, valores_enemy):
            if v_player > v_enemy:
                print("Você venceu!")  #VVai analisar carta contra para verificar qual a maior
                return "player"
            elif v_enemy > v_player:
                print("Inimigo venceu!")
                return "enemy"

        print("Empate!")
        return "empate"
    
    def definir_vencedor(cartas_player, cartas_enemy):
        resultado_player = Mao.avaliar(cartas_player)
        resultado_enemy  = Mao.avaliar(cartas_enemy)

        rank_player = Mao.RANKING_MAOS.index(resultado_player)
        rank_enemy  = Mao.RANKING_MAOS.index(resultado_enemy)

        print()
        print(f"A sua mão: ")
        for i in range(2):
            print(f"{cartas_player[i].getValue()} {cartas_player[i].getSuit()}")

        print()

        print(f"Mão do outro: ")
        for i in range(2):
            print(f"{cartas_enemy[i].getValue()} {cartas_enemy[i].getSuit()}")

        print()

        print(f"Mesa: ")
        for i in range(2, 7):
            print(f"{cartas_player[i].getValue()} {cartas_enemy[i].getSuit()}")

        print()
        if rank_player > rank_enemy:
            print("Você venceu!")
            
            return "player"
        elif rank_enemy > rank_player:
            print("Inimigo venceu!")
            return "enemy"
        else:
            return Mao.desempate(cartas_player, cartas_enemy)
