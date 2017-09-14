from Character import Character


class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__("Goblin", 6, 2)
        self.point_value = 2

    # def take_damage(self, damage):
    #     self.health -= damage
    #
    # def get_health(self):
    #     return (self.health)
    #
    # def is_alive(self):
    #     return (self.health > 0)
    def do_a_dance(self):
        print "The goblin is dancing.  You are mesmerized and stupified, but not hurt"
