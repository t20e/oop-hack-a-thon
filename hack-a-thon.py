class Player:
    def __init__(self,name,outfit,weapon):
        self.name = name
        self.outfit = outfit
        self.weapon = weapon


class Ninja(Player):
    def __init__(self,name,outfit,weapon,emoji,health,attack):
        super().__init__(name,outfit,weapon)
        self.emoji = emoji
        self.health = health
        self.attack = attack
    def attack_Ninja(self,Pirate):
        print('Ninja attacks')
        Pirate.health -= self.attack
        print(f'Pirates health is {Pirate.health}')
        print('****')
        if Pirate.health <= 0:
            self.village(self)
    def health_ninja(self):
        if Ninja.health <= 0:
            Ninja.village(self)
    def village(self,Pirate):
            print(f'ninja health is at {self.health} pirate conquers village {Pirate.emoji}')

class Pirate(Player):

    def __init__(self,name,outfit,weapon,emoji,health,attack):
        super().__init__(name,outfit,weapon)
        self.emoji = emoji
        self.health = health
        self.attack = attack
    def attack_1(self,Ninja):
        print('Pirate attacks')
        Ninja.health -= self.attack
        print(f'Ninjas health is at {Ninja.health}')
        print('****')
        if self.health <= 0:
            self.treasure(self)
    def health_1(self,Ninja):
        Pirate.health -= Ninja.attack
        if Ninja.health <= 0:
            print('****')
            Pirate.treasure()
    def treasure(self,Ninja):
            print(f'pirate health is at {self.health} ninja takes pirates treasure {Ninja.emoji}')


mark = Ninja('mark','ninja-yoroi','katana','🥷',55,100)
danny = Pirate('danny','full body velvet','axe','🏴‍☠️',80,30)
danny.attack_1(danny)
mark.attack_Ninja(mark)