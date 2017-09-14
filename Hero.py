from Character import Character


class Hero(Character):
    def __init__(self):
        super(Hero, self).__init__("Incognito", 6, 2)

        self.actions = ["Nothing", "Fight", "Flee"]
        self.items = []
        self.item_limit = 3

    def display_actions(self):
        i = 0
        for action in self.actions:
            i += 1
            print "<%d> %s" % (i, action)
        return i

    def cheer_for_hero(self):
        print "Hip Hip Hooray!! %s" % self.name

    def has_items(self):
        return(len(self.store) > 0)

    def display_items(self):
        if len(self.items) == 0:
            print "You have no items to display"
            return 0

        print "Item Inventory:"
        print "=" * len("Item Inventory:")
        item_number = 0
        for item in self.items:
            item_number += 1
            print "%d. %s" % item

        return(item_number)  # count of items

    def use_item(self):
        pass