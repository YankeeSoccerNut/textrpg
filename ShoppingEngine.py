
from Items import Items, Tonic, Sword


class ShoppingEngine(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Shopping.items => [Tonic, Sword]
    def __init__(self):
        self.items = [Tonic(), Sword()]

    def go_shopping(self, hero):
        print "====================="
        print "Welcome to the store!"
        print "====================="
        if not hero.has_coins():
            print "Thou art a beggar...be gone!"
            return

        while hero.has_coins():

            # if hero.has_items > hero.item_limit:
            #     print "You are fully loaded and cannot buy anything"
            #     break

            print "You have %d coins." % hero.coins
            print "What do you want to buy?"
            for i in xrange(len(self.items)):
                print "%d. buy %s (%d)" % (i + 1, self.items[i].name, self.items[i].cost)
            print "10. leave"
            input = int(raw_input("> "))

            if input == 10:
                break
            elif (input > len(self.items)):
                print "Invalid input"
            else:
                hero.buy_item(self.items[input - 1])

            if not hero.has_coins():
                print "Thank you for shopping here today.  We must make room fo r paying customers.  Come back when you have more coins!  A very large Ogre leads you out of the shop."

            # TODO: Good place for Ascii Art!!

    # def itemToBuy(self, item):
    #     if item == "Tonic":
    #         return Tonic()
    #     elif item == "Sword":
    #         return Sword()
    #     else:  # unknown item
    #         return None
