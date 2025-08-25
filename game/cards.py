class Cards:
    def __init__(self, name, description, attack=0, defense=0, life=0, stamina=0, poison=0):
        self.name = name
        self.description = description
        self.attack = attack
        self.defense = defense
        self.life = life
        self.stamina = stamina
        self.poison = poison
        
    def __str__(self):
        return f"{self.name} - {self.description}"


    @staticmethod
    def get_cards(): #Cards just can use when you have 25 stamina
        return [
            Cards("Fireball", "A powerful fire attack", attack=30),
            Cards("Shield", "Increases defense", defense=30),
            Cards("Heal", "Restores life", life=25),
            Cards("Buff Stamina", "Restores stamina", stamina=75),
            Cards("Veneno", "Drain life slowly", poison=5),
            Cards("Ice", "Ice rain", attack=28),
        ]
        
        
    def apply(self, user, target):
        if self.attack:
            target.life -= self.attack
            print(f"{user.name} caused {self.attack} damage to {target.name}")
        elif self.defense:
            user.defense += self.defense
            print(f"{user.name} inscreased defense by {self.defense}!")
        elif self.life:
            user.life += self.life
            print(f"{user.name} healed {self.life} life!")
        elif self.stamina:
            user.stamina += self.stamina
            print(f"{user.name} recovered {self.stamina} stamina!")
        elif self.poison:
            target.life -= self.poison
            print(f"{target.name} was poisoned and lost {self.poison} life!")
