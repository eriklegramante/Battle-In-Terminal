from character import Character
from battle import automatic_battle
import time
from colorama import Fore, Style, init
from utils   import show_status, divider

init(autoreset=True)  # Initialize colorama
player1 = Character("Hero", 100, 40, 30, 30) #name, life, attack, special attack, defense
player2 = Character("Villain", 100, 40, 30, 30)

divider()

while True:
    op = input("Choose a option: \n1. Manual Battle\n2. Automatic Battle\n3. exit\n> ")
    divider()

    if op not in ['1', '2', '3']:
        print(f" {Fore.RED}[INFO] Invalid option. Please choose 1, 2 or 3.")
        divider()

    if op == '1':
        print("Manual Battle Mode Selected")

    elif op == '2':
        automatic_battle(player1, player2)
        print("Automatic Battle Mode Selected")
        time.sleep(1)  # Pause for 1 second to simulate turn-based action

    elif op == '3':
        print("Exiting the game. Goodbye!")
        break