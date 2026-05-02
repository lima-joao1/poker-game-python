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
    if (player.getMoney() <= 0):
        print("Sem saldo para jogar.")
        return 
    
    print("Iniciando partida...")
    
    enemy = Player()
    enemy.addMoney(1000)

    baralho = Baralho()
    baralho.embaralhar()
    print("Baralho embaralhado!")
    print()

    for i in range(2):
        player.getMao().receberCarta(baralho.distribuir())
        enemy.getMao().receberCarta(baralho.distribuir())
    
    


def depositMoney(player):
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
        print(f"O seu saldo é de R$ {player.getMoney():.2f}")


player = Player()

menu(player)