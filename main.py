import json
import random

class Player(object):
    def __init__(self):
        with open("./player.json", "r") as f:
            self.playerData = json.load(f)

        self.profile = self.playerData['profile']
        self.sword = None
    def _profile(self):
        pass

    def _inventory(self):
        with open("./swords.json", "r") as f:
            self.inventory = json.load(f)

        self.sword = self.inventory[self.profile['sword']]

class Adventure(Player):
    def __init__(self):
        super().__init__()

        with open("./enemy.json", "r") as f:
            self.monsterData = json.load(f)

        self.monster = self.monsterData['Eastborne'][0]['slime']
        self.inBattle = True

    def _battle(self):
        if self.monster['hitpoint'] == 0:
            self.inBattle = False
            print("You won")
        else:
            dmg = random.randint(int(self.monster['damageMin']), int(self.monster['damageMax']))
            self.profile['hitpoint'] -= dmg
            print(self.sword)
            print(f"You received {dmg} damage and did {self.sword['damage']} damage")
            self.monster['hitpoint'] -= self.sword['damage']

class Main(Adventure):
    def __init__(self):
        super().__init__()
        self._inventory()

    def input(self, inp):
        if inp == 'adventure':
            self._battle()
            while self.inBattle == True:
                atkMode = input("Type 'atk': ")
                if atkMode:
                    self._battle()

inputDetector = input('Type your action: ')
play = Main().input(inputDetector)



