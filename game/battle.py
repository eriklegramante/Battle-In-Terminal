from utils import show_status, divider
import time
from colorama import Fore, Style, init


def automatic_battle(player1, player2):
    while True:
        turn = 1
        while player1.life > 0 and player2.life > 0:
            show_status(player1, player2, turn)

            if not player1.stamina >= 100:
                player1.attack_enemy(player2)
            else:
                player1.special_attack_enemy(player2)
            time.sleep(1)  # Pause for 1 second to simulate turn-based action
            if player2.life <= 0:
                print(Fore.GREEN + f"{player2.name} has been defeated! {player1.name} wins!" + Style.RESET_ALL)
                break
            
            if not player2.stamina >= 100:
                player2.attack_enemy(player1)
            else:
                player2.special_attack_enemy(player1)
            time.sleep(1)  # Pause for 1 second to simulate turn-based action
            if player1.life <= 0:
                print(Fore.GREEN + f"{player1.name} has been defeated! {player2.name} wins!" + Style.RESET_ALL)
                break

            turn += 1


def manual_battle(player1, player2):
    ...  # Placeholder for manual battle logic
    # This function can be implemented later if needed.