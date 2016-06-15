from game_objects import *
from enemy import *

class objFactory(): # <- this pattern allow to centralize the instatiation of diferent objects and diferent needs.
    def __init__(self):
        print("the game object factory was instantiated.")

    def create(self, obj): # <- each element created here needs some thing special.
        if obj=='excalibur':
            relic0 = relic()
            return excalibur(relic0)
        if obj=='golden_shield':
            gold0 = gold()
            return golden_shield(gold0)
        if obj=='merlin_wand':
            powder0 = powder()
            return merlin_wand(powder0)

class enemyFactory():
    def __init__(self):
        print("the game enemy factory was instantiated.")

    def create(self, enemy):
        if enemy=='easy_troll':
            return Enemy('little troll')
        if enemy=='easy_dragon':
            return Enemy('light dragon')
        if enemy=='easy_beast':
            return Enemy('little beast')
