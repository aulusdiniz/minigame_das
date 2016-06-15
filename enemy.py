class Enemy():
    def __init__(self, name='some_enemy'):
        self.name = name
        self.attack_points = 3
        self.defense_points = 5
        self.life = 50
        print('%s is now created  with %d life points.' % (self.name, self.life))

    def attack(self, target):
        print('enemy attack')
        target.gethit(self.attack_points)

    def gethit(self, atk):
        if self.life >= 0:
            damage = abs(self.defense_points - atk)
            self.life -= damage
        else:
            print("enemy killed!")
        print('%s life points is: %d' % (self.name, self.life))
