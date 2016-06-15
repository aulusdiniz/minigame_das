from hero import Hero
from enemy import Enemy
from game_objects import *
from objFactory import objFactory, enemyFactory

objFactory = objFactory()
enemyFactory = enemyFactory()

hero = Hero('Goku')
enemy = Enemy('Freeza')

hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)

objFactory.create('excalibur')
objFactory.create('golden_shield')
objFactory.create('merlin_wand')
sword = objFactory.create('excalibur')

hero.equip(sword)

enemyFactory.create('easy_troll')
enemyFactory.create('easy_beast')
enemyFactory.create('easy_dragon')
