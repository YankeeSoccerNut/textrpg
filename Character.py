import time

# Super class for all characters in the text rpg game


class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.point_value = 0

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

    def attack(self, enemy):
        if not self.is_alive():
            return

        print "%s attacks %s" % (self.name, enemy.name)
        enemy.take_damage(self.power)
        time.sleep(1.5)

    def take_damage(self, damage):
        self.health -= damage

    def get_health(self):
        return (self.health)

    def is_alive(self):
        return (self.health > 0)
