# This is just to gen a single mon For right now I am gonna quick and dirty copy and paste so I can use this tonight. Later I plan to put all the modules and classes in their own directory and import them from that location.

import random, sys, sqlite3, getopt
from collections import Counter

sys.path.insert(0, "modules/")

from monmods import Shiny
from monmods import RareRoll
from nature import Nature
from pokemon import Pokemon

# To call this program do the following from CLI python pokemon.py PokemonName(Currently Cap sensitive) Level

mon = sys.argv[1]
level = sys.argv[2]

pokemon = Pokemon(mon, level)


print pokemon

print Counter(pokemon.Naturalize())


print sorted(pokemon.LevelUp().values(), reverse=True)

