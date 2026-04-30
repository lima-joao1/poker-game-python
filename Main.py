from Baralho import Baralho
from Carta import Carta
from Player import Player

def menu(player):
    while True:
        print()
        print("****POKER HOLD'EM****")
        print("1 - Iniciar jogo")
        print("2 - Depositar dinheiro")
        print("3 - Sacar dinheiro")
        print("4 - Mostrar saldo")
        print("0 - Sair do jogo")
        print()
        command = int(input("Digite o comando [0-4]: "))
        print()

        if (command == 0):
            break

        command_manager(command, player)

def start_game(player):
    if (player.getAge() < 18):
        print("Menores de idade não podem jogar.")

def depositMoney(player):
    cardNumber = int(input("Digite o número do cartão: "))
    cvv = int(input("Digite o CVV: "))
    validation = (input("Data de validade do cartão (mm/yy): "))

    money = int(input("Valor a ser depositado: R$ "))

    player.addMoney(money)


def command_manager(command, player):
    if (command == 1):
        start_game(player)
    
    elif (command == 2):
        depositMoney(player)
        
    elif (command == 3):
        print("Não foi possível sacar.")

    elif (command == 4):
        print(f"O saldo de {player.getName().capitalize()} é de R$ {player.getMoney():.2f}")


playerName = input("Digite o nome do jogador: ")
playerAge = int(input("Digite sua idade: "))
print()
player = Player(playerName, playerAge)

menu(player)