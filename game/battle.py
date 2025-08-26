from utils import show_status, show_status_manual, divider, show_status_manual_started
import time
from colorama import Fore, Style
from cards import Cards
import random


class Battle:
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
        # Nomes dos jogadores
        player1.name = input("🧑 Please enter with your nickname player 1: ").strip().capitalize()
        player2.name = input("🧑 Please enter with your nickname player 2: ").strip().capitalize()
        divider()

        # Sorteia quem começa
        current_player = random.choice([player1, player2])
        other_player = player2 if current_player == player1 else player1
        print(Fore.GREEN + f"🎲 {current_player.name} will start the match!" + Style.RESET_ALL)
        print(Fore.GREEN + "⚔️  The battle has begun!" + Style.RESET_ALL)
        divider()
        show_status_manual_started(player1, player2)

        turn = 1
        while player1.life > 0 and player2.life > 0:
            divider()
            print(Fore.CYAN + f"🔄 Turn {turn}: {current_player.name}, it's your turn!" + Style.RESET_ALL)

            action = input("Choose an action:\n1️⃣  Attack\n2️⃣  Use Magic Card (requires 50 stamina)\n3️⃣  Exit game\n> ").strip()

            if action not in ['1', '2', '3']:
                print(Fore.RED + "⚠️ [INFO] Invalid option. Please choose 1, 2 or 3." + Style.RESET_ALL)
                continue

            if action == '1':
                current_player.attack_enemy(other_player)

            elif action == '2':
                if current_player.stamina >= 50:
                    print(Fore.YELLOW + f"🃏 {current_player.name}, your available Cards:")
                    deck = Cards.get_cards()
                    hand = random.sample(deck, 3)

                    for i, card in enumerate(hand, 1):
                        print(f"{i}. {card}")

                    choice = input("👉 Choose a card (1-3): ")
                    if choice in ['1','2','3']:
                        chosen_card = hand[int(choice)-1]
                        print(Fore.CYAN + f"✨ {current_player.name} used {chosen_card.name}!" + Style.RESET_ALL)
                        chosen_card.apply(current_player, other_player)
                        current_player.stamina -= 50
                    else:
                        print(Fore.RED + "❌ Invalid choice. You lost your turn!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"⛔ Not enough Stamina ({current_player.stamina}/50)." + Style.RESET_ALL)
                    print(Fore.RED + "❌ You lost your turn!" + Style.RESET_ALL)

            elif action == '3':
                print(Fore.MAGENTA + f"🏳️  {current_player.name} gave up! 🏆 {other_player.name} wins!" + Style.RESET_ALL)
                break

            show_status_manual(player1, player2, turn)
            turn += 1

            current_player, other_player = other_player, current_player

        if player1.life <= 0:
            print(Fore.RED + f"☠️ {player1.name} was defeated! 🏆 {player2.name} wins!" + Style.RESET_ALL)
        elif player2.life <= 0:
            print(Fore.RED + f"☠️ {player2.name} was defeated! 🏆 {player1.name} wins!" + Style.RESET_ALL)