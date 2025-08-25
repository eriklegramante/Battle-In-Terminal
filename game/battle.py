from utils import show_status, show_status_manual, divider
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
        player1.name = input("Please enter with your nickname player 1: ")
        player2.name = input("Please enter with your nickname player 2: ")

        # Sorteia quem começa
        current_player = random.choice([player1, player2])
        opponent = player2 if current_player == player1 else player1
        print(Fore.GREEN + f"{current_player.name} was drawn to start!" + Style.RESET_ALL)

        turn = 1
        while player1.life > 0 and player2.life > 0:
            divider()
            print(Fore.CYAN + Style.BRIGHT + f"TURN {turn} - Your turn: {current_player.name}" + Style.RESET_ALL)

            # --- Jogada do jogador atual ---
            atk = input("1. Normal attack \n2. Use Cards \n> ")

            if atk == '1':
                current_player.attack_enemy(opponent)

            elif atk == '2':
                if current_player.stamina >= 50:
                    print("Your available cards:")
                    deck = Cards.get_cards()
                    hand = random.sample(deck, 3)

                    for i, card in enumerate(hand, 1):
                        print(f"{i}. {card}")

                    choice = input("Choose a card (1-3): ")
                    if choice in ['1', '2', '3']:
                        chosen_card = hand[int(choice)-1]
                        print(Fore.CYAN + f"{current_player.name} used {chosen_card.name}!" + Style.RESET_ALL)
                        chosen_card.apply(current_player, opponent)
                        current_player.stamina -= 50
                    else:
                        print(Fore.RED + "Invalid card choice! You lost your turn." + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"You can't use a card, not enough stamina ({current_player.stamina}/50)" + Style.RESET_ALL)

            else:
                print(Fore.RED + "Invalid option! You lost your turn." + Style.RESET_ALL)

            # --- Mostrar status depois da ação ---
            show_status_manual(player1, player2, turn)

            # Verifica vitória
            if opponent.life <= 0:
                print(Fore.GREEN + f"{opponent.name} has been defeated! {current_player.name} wins!" + Style.RESET_ALL)
                break

            # Troca jogadores (sempre acontece no fim do turno)
            current_player, opponent = opponent, current_player
            turn += 1