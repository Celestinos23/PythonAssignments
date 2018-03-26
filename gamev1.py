#Name: PYTHON FINAL GAME
#Date: 2018-03-26
#Introduction to programming final assignment
#Description: Text-based jungle adventure game


from random import randint
import time


def Introduction():  #Intro to the game.
    print('''The jungle is pure magic at night. It is filled with insects, birds, gorillas,
and tigers. A hidden world in perfect balance until the evil animal Poachers appear.
They kill everything in their path to take animal treasures and sell them to collectors.
What they don't expect is the jungle animals coming together to fight back and save themselves.\n''')


def Manual(): #What the game does and how to win it.
    print('''This is a text based game where you fight poachers as a Gorilla. Scare 2 of them to win the game!''')



Introduction()

time.sleep(2) #Wait two seconds and print manual
Manual()


class Character:
    def __init__(self):
        self.name = ""
        self.hp = 1
        self.hp_max = 1

    def do_damage(self, enemy):
        damage = min(max(randint(0, self.hp) - randint(0, enemy.hp), 0), enemy.hp)
        enemy.hp = enemy.hp - damage

        if damage == 0:
            print('{} dodge {} attack'.format(enemy.name, self.name))
        else:
            print('{} injure {}'.format(self.name, enemy.name))
            return enemy.hp <= 0


class Enemy(Character):
    def __init__(self, player):
        super().__init__()
        self.name = 'Poacher'
        self.hp = randint(1, 20)


class Player(Character):
    def __init__(self):
        super().__init__()
        self.state = 'normal'
        self.hp = 20
        self.hp_max = 20

    def quit(self):
        print ('{} All the animals were caught by the poachers \nR.I.P.'.format(self.name))
        self.hp = 0

    def options(self):
        print (Commands.keys())

    def status(self):
        print ('{} health: {}/{}'.format(self.name, self.hp, self.hp_max))

    def tired(self):
        print ('{} feels tired'.format(self.name))
        self.hp = self.hp - 3

    def boost(self):
        if self.state != 'normal':
            print ('{} Can\'t boost energy while you\'re fighting'.format(self.name))
            self.enemy_attacks()

        else:
            print ('{} Boosting energy!'.format(self.name))
            if randint(0, 1):
                self.enemy = Enemy(self)
                print ('Oh no! {} is rudely awakened by {}'.format(self.name, self.enemy.name))
                self.state = 'fight'
                self.enemy_attacks()
            else:
                if self.hp < self.hp_max:
                    self.hp = self.hp + 5

                else:
                    print ('{} slept too much'.format(self.name))
                    self.hp = self.hp - 3

    def explore(self):

        if self.state != 'normal':
            print ('{} is too busy right now! try something else'.format(self.name))
            self.enemy_attacks()

        else:
            print ('{} explores the jungle, sunny day, can feel the peace'.format(self.name))
            if randint(0, 1):
                self.enemy = Enemy(self)
                print ('{} encounters {} time to fight!'.format(self.name, self.enemy.name))
                self.state = 'fight'

            else:
                if randint(0, 1):
                    self.tired()

    def run(self):

        if self.state != 'fight':
            print ('{} run into nothing...'.format(self.name, self.tired()))

        else:
            if randint(1, self.hp) > randint(1, self.enemy.hp):
                print ('{} run from {}'.format(self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'

            else:
                print ('{} couldn\'t escape from {}!'.format(self.name, self.enemy.name))
                self.enemy_attacks()

    def attack(self):
        if self.state != 'fight':
            print('{} attack to the air, Gorilla is confused'.format(self.name, self.tired()))

        else:
            if self.do_damage(self.enemy):
                print ('{} frighten the {} !'.format(self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
                if randint(0, self.hp) < 100:
                    self.hp = self.hp
                    self.hp_max = self.hp_max
                    print ('{} feels stronger, feels safe.'.format(self.name))

            else:
                self.enemy_attacks()

    def enemy_attacks(self):
            if self.enemy.do_damage(self):
                print('{} was slaughtered by {} !!!\nR.I.P.'.format(self.name, self.enemy.name))


Commands = {
      'quit': Player.quit,
      'status': Player.status,
      'boost': Player.boost,
      'explore': Player.explore,
      'run': Player.run,
      'attack': Player.attack,
      }


p = Player()
p.name = input('Hey Gorilla, what\'s your name? \n')

print('\n{} Enters the Jungle, ready to fight the poachers and save the animals.'.format(p.name))

while(p.hp > 0):
    print ('\nList of actions')
    print(Commands.keys())
    line = input('>')
    time.sleep(0.5)
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                Commands[c](p)
                commandFound = True
                break

    if not commandFound:
                print ('{} doesn\'t understand the suggestion'.format(p.name))
