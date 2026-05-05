from Baralho import Baralho
from Mao import Mao
from Player import Player
from Mesa import Mesa

def menu(player):
    while True:
        print()
        print("**** POKER HOLD'EM ****")
        print()
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
    if (player.getMoney() <= 20):
        print("Sem saldo para jogar.")
        return 
    
    print("Iniciando partida...")
    
    enemy = Player()
    enemy.addMoney(1000)
    mesa = Mesa()

    darCartas(player, enemy, mesa)

    while True:
        print(f"Suas cartas: {player.getMao().mostrar()}")
        print(f"Mesa: {mesa.mostrar()}")
        print()
        print("O inimigo começa apostando R$ 20.00")
        print("Você pode cobrir, aumentar ou correr.")
        print()

        bet_enemy = enemy.betMoney(20)
        pot = bet_enemy

        cartas_player = player.getMao().getCartas() + mesa.getCartas()
        cartas_enemy = enemy.getMao().getCartas() + mesa.getCartas()

        print("1 - Cobrir a aposta")
        print("2 - Aumentar a aposta")
        print("3 - Correr")

        action = int(input("Escolha sua ação [1-3]: "))

        if (action == 3):
            print("Rodada finalizada.")
            player.getMao().limpar()
            enemy.getMao().limpar()
            darCartas(enemy, mesa)
            break

        action_manager(bet_enemy, pot, player, action, cartas_player, cartas_enemy, enemy)

        answer = input("Deseja jogar novamente? (Y/N): ").upper()
        
        player.getMao().limpar()
        enemy.getMao().limpar()
        mesa.getCartas().clear()
        
        if (answer == "Y" and player.getMoney() > 0):
            darCartas(player, enemy, mesa)
            continue
        else:
            print("Jogo finalizado.")
            break
    
def darCartas(player, enemy, mesa):

    baralho = Baralho()
    baralho.embaralhar()
    print("Baralho embaralhado!")
    print()

    for i in range(2):
        player.getMao().receberCarta(baralho.distribuir())
        enemy.getMao().receberCarta(baralho.distribuir())
    
    for i in range(5):
        mesa.receberCarta(baralho.distribuir())

def action_manager(bet_enemy, pot, player, action, cartas_player, cartas_enemy, enemy):
    
    if (action == 1):
        pot = cobrir(bet_enemy, player, pot)

    elif (action == 2):
        pot = aumentar(pot, player, enemy)
        
    vencedor = Mao.definir_vencedor(cartas_player, cartas_enemy)
    if (vencedor == "player"):
        player.addMoney(pot)
    elif (vencedor == "enemy"):
        enemy.addMoney(pot)

def cobrir(bet_enemy, player, pot):
    aposta_player = player.betMoney(bet_enemy)
    pot += aposta_player
    print(f"Você cobriu R$ {bet_enemy:.2f}. O valor total é de R$ {pot:.2f}")
    return pot

def aumentar(pot, player, enemy):
    while True:
        aposta_player = (int(input("Valor a ser aumentado: R$ ")))
        
        if (aposta_player > player.getMoney()):
            print(f"Saldo não suficiente. Você só tem R$ {player.getMoney():.2f}")
            continue
        
        player.betMoney(aposta_player)
        break

    pot = aposta_player

    enemy.betMoney(aposta_player)
    pot += aposta_player

    print(f"Aposta aumentada. O valor total é de R$ {pot:.2f}")
    return pot

def depositMoney(player):
    entrada = input("Valor a ser depositado: R$ ")
    money = int(entrada) if entrada else 1000

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