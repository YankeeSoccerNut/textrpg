# Contrib modules
# Core
import os
from random import randint

# 3rd Party

# Custom modules
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from BattleEngine import BattleEngine

hero = Hero()
monsters = []  # list of monsters

# Before the game starts, let's ask the hero for his or her name.
print "What is thy name, brave adventurer?"
hero.name = raw_input("> ")
hero.cheer_for_hero()


print "Where shall your quest take place?"
quest_location = raw_input("> ")

print """
 |||            _.'   _      _.-. |        | |--
\|||         _.'    -    _.-'  _|-|       -| |__
 ||;-,    _.'   '-  _.-'' _.-''|  |-'      | `._
-'| / \_,' _    _.-'   _.' |   |  |    -|  |
----|,`   |  _.'   _.-' | ,| ,'| _| |      |_
   _:  _   ,'   .-'    _|/ \ | | -|  _|_   | '
  | |    ,'  .-'     , )|)-( |_|  |-       |    -
-   |  ,'  ,'(   `  /_\||`.'   |- |   -|_  |
___-| /  ,'   )     `.'||.-| _ | ||        | '-'
__( |;  /    / ,-    | ||  |/ \|_ | _|    -|
  | :  ; ,-.-)       | ||  || ||  |   |_   |    _
 _| | :/` _..\  `-.  | ||__||_|;--;--------:  ,'`
  | | |,-'  _/       |,-/\_|  /__/__________\::::
  |-| |   ,' \, ` ___|||||-|  |  |  _|_     ||___
_ | | | ,'   (   ;   :'''' /| ||_|       _  ||---
- | | |/     ;  /     :   : | |  |   _|_    ||---
  | | |      |,'______|-..| | |_||      |  _||---
  | | |      ||_      |   | | |_ |  -      -|----
_|| | |      ;|-:  _  |   | |,|- |-   _|  _ |--,'
  | | |______\| |,' `.|`-.| |:|  | _|    |  |,','
  |-| | ~   ~|| ||__|||! !| | ;--;----__---,','|
  | | |,._,~_|:.||-'|||! !| |/__/____/\_\,','|\|
-.| | ;     _.-'|| - ||`.!| ||  |    ||_|,'| | |,
 || ;'|_,-''    -    - `.`| ||  | ___|| ||\| |,',
, | | |    -     -     -  ) '|__||\  || | \|,','
  ; | | -     -      -      |\    \\ || |_,','
 /| | ;    -     -           \\    \\|| |','
/ | |/                        \\    \|| |'
"""

print "How many monsters are you will to fight, brave %s?" % hero.name
number_of_enemies = int(raw_input("> "))

# Load up the monster table based on user input...randomize which monster
for i in range(0, number_of_enemies):
    rand_num = randint(0, 1)
    if(rand_num == 1):
        monsters.append(Goblin())
    else:
        monsters.append(Vampire())

# Let the battles begin!

battleEngine = BattleEngine()

for i, monster in enumerate(monsters):  # enumerate
    hero_won = battleEngine.battle(hero, monster)

    if not hero_won or not hero.is_alive():
        print "These foes have proven to be too powerful for you.  Better luck next time!"
        break
    elif i < len(monsters):
        print "You won a battle...shopping time!"
        # shopping_engine.do_shopping(hero)

if hero.is_alive():
    print "Congratulations, %s , you defeated %d enemies and live to fight another day!" % (hero.name, i + 1)

battleEngine.display_battles()
