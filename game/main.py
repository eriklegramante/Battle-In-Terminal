from character import Character
from battle import Battle
import time
from colorama import Fore, Style, init
from utils import divider, reset_players

init(autoreset=True)
player1 = Character("Hero", 200, 40, 30, 30) #name, life, attack, special attack, defense
player2 = Character("Villain", 200, 40, 30, 30)

divider()

while True:
    op = input("Choose a option: \n1. Manual Battle\n2. Automatic Battle\n3. Rules \n4. Exit\n> ")
    divider()

    if op not in ['1', '2', '3', '4']:
        print(Fore.RED + "[INFO] Invalid option. Please choose 1, 2, 3 or 4." + Style.RESET_ALL)
        divider()
        continue 
    
    if op == '1':
        player1, player2 = reset_players()
        print(Fore.CYAN + "Manual Battle Mode Selected" + Style.RESET_ALL)
        Battle.manual_battle(player1, player2)
        time.sleep(1)

    elif op == '2':
        print(Fore.CYAN + "Automatic Battle Mode Selected" + Style.RESET_ALL)
        time.sleep(1)
        Battle.automatic_battle(player1, player2)

    elif op == '3':
        rules = """Game Rules:
        
1. Each player starts with 400 life points.
2. Players take turns to attack each other.
3. Each attack increases the player's stamina by 25 points.
4. When a player's stamina reaches 50 points, they can use a magic card.
5. When a player's life points drop to 0, they lose the game.
6. The game continues until one player is defeated.
7. If you choose a wrong option, you will lose your turn."""
        print(Fore.YELLOW + rules + Style.RESET_ALL)
        divider()

    elif op == '4':
        print(Fore.MAGENTA + "Exiting the game. Goodbye!" + Style.RESET_ALL)
        break