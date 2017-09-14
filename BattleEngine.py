import time


class BattleEngine(object):
    def __init__(self):
        self.outcomes = []  # track outcomes for replay/retell??

    def battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.is_alive() and enemy.is_alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            hero.display_actions()
            input = int(raw_input("Choose by number...and choose wisely! > "))

            if input == 2:
                hero.attack(enemy)
            elif input == 1:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue

            if enemy.is_alive():  # payback!
                enemy.attack(hero)
                # self.logBattle(hero, enemy, "WEAPON", hero_won)

        if hero.is_alive():
            print "You defeated the %s!!" % enemy.name
            #self.logBattle(hero, enemy, "WEAPON", hero_won)
            return True
        else:
            print "You lost this battle with the %s. :-(" % enemy.name
            #self.logBattle(hero, enemy, "WEAPON", hero_won)
            return False

    def logBattle(self, hero, enemy, hero_won):
        self.outcomes.append([hero, enemy, "WEAPON", hero_won])

    def display_battles(self):
        for i, battle in enumerate(self.outcomes):
            print "Battle %d:  %r" % (i, battle)

        return len(self.outcomes)
