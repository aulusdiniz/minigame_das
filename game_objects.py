class excalibur():
    def __init__(self, relic): # each object needs a diferent item to be made.
        self.name = 'excalibur'
        self.power = 4
        self.durability = 30
        self.relic = relic  # <- here is where the item is used for example.
        print("this is excalibur, the king sword.")

    def description(self):
        print("this is excalibur, the king sword.")

class golden_shield():
    def __init__(self, gold_used):
        self.name = 'golden shield'
        self.power = 8
        self.durability = 100
        self.gold = gold_used
        print("a shield made from dragon's gold")

    def description(self):
        print("a shield made from dragon's gold")

class merlin_wand():
    def __init__(self, powder):
        self.name = 'merlin wand'
        self.power = 10
        self.durability = 200
        self.powder = powder
        print("the magic wand used by merlin, the greatest.")

    def description(self):
        print("the magic wand used by merlin, the greatest.")

class relic():
    def __init__(self):
        print("a new relic was made.")

class gold():
    def __init__(self):
        print("just the right amount of gold to a shield was made.")

class powder():
    def __init__(self):
        print("you collected the magic powder to make a magic wand.")
