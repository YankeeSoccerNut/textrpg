from Character import Character


class Vampire(Character):
    def __init__(self):
        super(Vampire, self).__init__("Vampire", 15, 4)
        self.point_value = 5

    def make_girls_swoon(self):
        print "The skin of the vampire sparkles like diamonds.  All the girls swoon."
