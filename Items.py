
# Feels like I'm trying to implement a Factory pattern for items....


class Items(object):
    def __init__(self):
        self.name = ""
        self.cost = 0
        self.power_effects = 0
        self.health_effects = 0

    # def factory(self, type):
    #     print "In factory method...%r" % (type)
    #
    #     if type == 'Items':
    #         return
    #     elif type == 'Tonic':
    #         self.name = type
    #         self.cost = 5
    #         self.power_effects = 0
    #         self.health_effects = 2
    #     elif type == 'Sword':
    #         self.name = type
    #         self.cost = 10
    #         self.power_effects = 2
    #         self.health_effects = 0
    #     else:  # invalid type
    #         return None

    def apply(self, character):
        character.health += self.health_effects
        character.power += self.power_effects
        print "Applied %s.  Health Effect %d, Power Effect %d" % (self.name, self.health_effects, self.power_effects)


class Tonic(Items):
    def __init__(self):
        # Call the init of this classes super class (Items)
        super(Tonic, self).__init__()

        self.name = "Tonic"
        self.cost = 5
        self.power_effects = 0
        self.health_effects = 2

    def __repr__(self):
        return "repr.Tonic"


class Sword(Items):
    def __init__(self):

        super(Sword, self).__init__()
        self.name = "Sword"
        self.cost = 10
        self.power_effects = 2
        self.health_effects = 0

    def __repr__(self):
        return "repr.Sword"

# class Map(Item)
