from character import character
import time # Adding a small delay for better readability of output

player1 = character("Hero", 100, 40, 30, 30) #name, life, attack, special attack, defense
player2 = character("Villain", 100, 40, 30, 30)


while player1.life > 0 and player2.life > 0:
    player1.attack_enemy(player2)
    time.sleep(1)  # Pause for 1 second to simulate turn-based action
    player2.show_life()
    
    if player2.life <= 0:
        print(f"{player2.name} has been defeated! {player1.name} wins!")
        break
    
    player2.attack_enemy(player1)
    time.sleep(1)  # Pause for 1 second to simulate turn-based action
    player1.show_life()
    
    if player1.life <= 0:
        print(f"{player1.name} has been defeated! {player2.name} wins!")
        break

    player1.show_stamina()
    player2.show_stamina()