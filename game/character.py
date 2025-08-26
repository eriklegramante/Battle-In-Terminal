from random import randint
from colorama import Fore, Style

class Character:
    def __init__(self, name, life, attack, special_attack, defense, stamina=0):
        self.name = name
        self.life = life
        self.attack = attack
        self.special_attack = special_attack
        self.defense = defense
        self.stamina = stamina

    def attack_enemy(self, enemy):
        damage = randint(15, self.attack) - randint(5, enemy.defense)
        if damage < 1:
            damage = 0
        else:
            if damage >= 12:
                self.stamina += 25
                if self.stamina > 100:
                    self.stamina = 100
        enemy.life -= damage

        if damage == 0:
            print(Fore.RED + f"💨 {self.name} attacks {enemy.name} but it was ineffective! {Style.RESET_ALL}")
        else:
            print(Fore.YELLOW + f"⚔️  {self.name} attacks {enemy.name} for {damage} damage! "
                  f"(🔥 Stamina: {self.stamina})" + Style.RESET_ALL)

    def special_attack_enemy(self, enemy):
        if self.stamina >= 100:
            base = randint(20, 40) + self.special_attack
            damage = base - randint(5, enemy.defense)
            if damage < 1:
                damage = 0
            enemy.life -= damage
            self.stamina = 0
            print(Fore.MAGENTA + f"🌟 {self.name} uses a SPECIAL ATTACK on {enemy.name} "
                  f"for {damage} damage! (🔥 Stamina reset to {self.stamina})" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + f"⏳ {self.name} doesn't have enough stamina yet! "
                  f"({self.stamina}/100)" + Style.RESET_ALL)

    def show_stamina(self):
        print(Fore.BLUE + f"🔥 {self.name} has {self.stamina} stamina." + Style.RESET_ALL)
        if self.stamina >= 100:
            print(Fore.GREEN + f"⚡ {self.name} can use a SPECIAL ATTACK!" + Style.RESET_ALL)

    def show_life(self):
        if self.life > 0:
            print(Fore.GREEN + f"💖 {self.name} has {self.life} life." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"☠️ {self.name} has been defeated!" + Style.RESET_ALL)
