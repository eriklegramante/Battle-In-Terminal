from character import character
import time # Adding a small delay for better readability of output
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama
player1 = character("Hero", 100, 40, 30, 30) #name, life, attack, special attack, defense
player2 = character("Villain", 100, 40, 30, 30)

def divider():
    print("=" * 30)


def show_status(p1, p2, turn):
    divider()
    print(Fore.CYAN + Style.BRIGHT + f"TURN {turn}" + Style.RESET_ALL)
    print(f"{p1.name}: {Fore.RED}♥ {p1.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p1.stamina}{Style.RESET_ALL}")
    print(f"{p2.name}: {Fore.RED}♥ {p2.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p2.stamina}{Style.RESET_ALL}")
    divider()


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