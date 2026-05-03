import random

def menu():
    print(
        "1. Proxima Rodada"
    )

def criar_baralho():
    Naipes = ['Ouro', 'Copas', 'Paus', 'Espadas']
    Valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']

    Baralho = []

    for n in Naipes:
        for v in Valores:
            cartas = (v,n)
            Baralho.append(cartas)
    
    return Baralho

def pegar_carta(Baralho):
    PlayerHand = []

    for n in range (2):
        carta = random.choice(Baralho)
        PlayerHand.remove(carta)
        PlayerHand.append(carta)

    print(PlayerHand)

CartasMesa = []

def mesa_rodada1(Baralho):
    
    for n in range (3):
        carta = random.choice(Baralho)
        Baralho.remove(carta)
        CartasMesa.append(carta)

    print(CartasMesa)

def mesa_proxrodadas(Baralho):
    
    carta = random.choice(Baralho)
    Baralho.remove(carta)
    CartasMesa.append(carta)


"""def comparar():"""