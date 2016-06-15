class Hero():
    def __init__(self, name='some_hero'):
        self.name = name
        self.attack_points = 10
        self.defense_points = 10
        self.life = 100
        self.equips = None
        print('hero is now created with %d life points.' % self.life)

    def attack(self, target):
        print('hero attack')
        target.gethit(self.attack_points)

    def gethit(self, atk):
        if self.life >= 0:
            damage = abs(self.defense_points - atk)
            self.life -= damage
        else:
             print("you are dead.")
        print('%s life points is: %d' % (self.name, self.life))

    def equip(self, item):
        self.equips = item
        print ("you are now equiped with %s" % self.equips.name)
