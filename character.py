from random import randint

class character:
    def __init__(self, name, life, attack, special_attack, defense, stamina= 0):
        self.name = name
        self.life = life
        self.attack = attack
        self.special_attack = special_attack
        self.defense = defense
        self.stamina = stamina

    def attack_enemy(self, enemy): #attack when stamina reaches 100 (+25 per attack)
        damage = randint(10, self.attack) - randint(5, self.defense)
        if damage < 1:
            damage = 0
        else:
            if damage >= 5:
                self.stamina += 25
                if self.stamina > 100:
                    self.stamina = 100
        enemy.life -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage! (stamina: {self.stamina})")

    
    def special_attack_enemy(self, enemy): #attack when stamina reaches 100 (+25 per attack)
        if self.stamina >= 100:
            base = randint(20, 40) + self.special_attack
            damage = base - randint(5, enemy.defense)
            if damage < 1:
                damage = 0
            enemy.life -= damage
            self.stamina = 0
            print(f"{self.name} uses special attack on {enemy.name} for {damage} damage! (stamina: {self.stamina})")
        else:
            print(f"{self.name} doesn't have enough stamina yet! ({self.stamina}/100)")


    def show_stamina(self):
        if self.stamina <= 100:
            print(f"{self.name} has {self.stamina} stamina.")
            print(f"{self.name} can use special attack.")


    def show_life(self):
        if self.life > 0:
            print(f"{self.name} has {self.life} life.")
        else:
            print(f"{self.name} has been defeated!")