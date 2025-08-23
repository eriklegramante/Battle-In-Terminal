from utils import show_status, divider
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
        while True:
            player1.name = input("Please enter with your nickname player 1: ")
            player2.name = input("Please enter with your nickname player 2: ")
        
            drawn_player = random.choice([player1, player2])
            print(Fore.GREEN + f"{drawn_player.name} was drawn! ")

            turn = 1
            while player1.life > 0 and player2.life > 0:
                show_status(player1, player2, turn)
                
                if drawn_player == player1:
                    atk = input(f"1. Normal attack \n2. Use Cards \n> ")

                    if atk not in ['1', '2']:
                        print(Fore.RED + "[INFO] Invalid option. Please choose 1 or 2.")
                        continue

                    if atk == '1':
                        player1.attack_enemy(player2)

                    elif atk == '2':
                        if player1.stamina >= 25:
                            print("Your available cards:")
                            deck = Cards.get_cards()
                            hand = random.sample(deck, 3)

                            for i, card in enumerate(hand, 1):
                                print(f"{i}. {card}")

                            choice = input("Choose a card (1-3): ")
                            if choice in ['1', '2', '3']:
                                chosen_card = hand[int(choice)-1]
                                print(Fore.CYAN + f"{player1.name} used {chosen_card.name}!")

                                # Aqui aplicamos os efeitos da carta (simplificado)
                                if chosen_card.attack:
                                    player2.life -= chosen_card.attack
                                if chosen_card.defense:
                                    player1.defense += chosen_card.defense
                                if chosen_card.life:
                                    player1.life += chosen_card.life
                                if chosen_card.stamina:
                                    player1.stamina += chosen_card.stamina
                                if chosen_card.poison:
                                    player2.life -= chosen_card.poison
                                
                                player1.stamina -= 25  # gastar stamina para usar carta
                            else:
                                print(Fore.RED + "Invalid card choice!")

                        else:
                            print(Fore.RED + f"You can't use a Card, not enough stamina: {player1.stamina}")