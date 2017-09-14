from Character import Character


class Wizard(Character):
    def __init__(self):
        super(Wizard, self).__init__("Wizard", 20, 5)
        self.point_value = 10
        self.spells[5, 10, 15, 20]

    def cast_a_spell(self, enemy):
        print "The Wizard casts a spell"

    def attack(self, enemy):
        if not self.is_alive():
            return
