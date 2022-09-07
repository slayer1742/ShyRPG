import json
import random
import time

class Player(object):
    def __init__(self):
        with open("./db/player.json", "r") as f:
            self.playerData = json.load(f)

        self.player = self.playerData['profile']
        self.sword = None

    def _inventory(self):
        with open("./db/swords.json", "r") as f:
            self.inventory = json.load(f)

        self.sword = self.inventory[self.player['equepments']['sword']]

    def _Profile(self):
        print(f"Rank: {self.player['rank']['title']} \nLevel {self.player['rank']['level']}")

class Adventure(Player):
    def __init__(self):
        super().__init__()

        with open("./db/enemy.json", "r") as f:
            self.monsterData = json.load(f)

        self.monster = self.monsterData['Eastborne'][0]
        self.inBattle = False

    def _AdvStart(self):
        print("You went on a great adventure...")
        time.sleep(2)

        print(f"You encounted a {self.monster['name']}")
        if self.inBattle == False:
            self.inBattle = True

    def _Battle(self):
        self._Attack()

        if int(self.player['hitpoint']) <= 0:
            self.inBattle = False
            print("You Died")

            returnTown = input("Press Enter to continue...")
            if returnTown:
                pass

        if int(self.monster['hitpoint']) <= 0:
            self.inBattle = False
            print(f"{self.monster['name']} felted")

    def _Attack(self):
        dmg = random.randint(int(self.monster['damageMin']), int(self.monster['damageMax']))
        self.player['hitpoint'] -= dmg

        print(f"You received {dmg} damage and did {self.sword['damage']} damage")
        self.monster['hitpoint'] -= self.sword['damage']

class Map(object):
    def __init__(self):
        pass

class Main(Adventure):
    def __init__(self):
        super().__init__()
        self._inventory()

    def _MainFrame(self):
        actionAdd = input('Type your action: ')
        if actionAdd:
            self._Actions(actionAdd)

    def _Actions(self, inp):
        if inp == 'adventure' or inp == 'adv':
            self._AdvStart()
            while self.inBattle == True:
                atkMode = input("Type 'atk' to attack: ")
                if atkMode:
                    self._Battle()

        elif inp == 'profile':
            self._Profile()

play = Main()._MainFrame()