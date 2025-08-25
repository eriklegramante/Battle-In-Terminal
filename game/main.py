from character import Character
from battle import Battle
import time
from colorama import Fore, Style, init
from utils import divider, reset_players

init(autoreset=True)  # Initialize colorama
player1 = Character("Hero", 400, 40, 30, 30) #name, life, attack, special attack, defense
player2 = Character("Villain", 400, 40, 30, 30)

divider()

while True:
    op = input("Choose a option: \n1. Manual Battle\n2. Automatic Battle\n3. Exit\n> ")
    divider()

    if op not in ['1', '2', '3']:
        print(Fore.RED + "[INFO] Invalid option. Please choose 1, 2 or 3." + Style.RESET_ALL)
        divider()
        continue 
    
    if op == '1':
        player1, player2 = reset_players()
        Battle.manual_battle(player1, player2)
        print(Fore.CYAN + "Manual Battle Mode Selected" + Style.RESET_ALL)
        time.sleep(1)

    elif op == '2':
        print(Fore.CYAN + "Automatic Battle Mode Selected" + Style.RESET_ALL)
        time.sleep(1)
        Battle.automatic_battle(player1, player2)

    elif op == '3':
        print(Fore.MAGENTA + "Exiting the game. Goodbye!" + Style.RESET_ALL)
        break
