# This is a script to gen wild pokemon encounters for Pokemon the TableTop Game
# This iteration includes all pokemon from Omega Ruby/Saphire (NO WILD MEGALUTIONS!)
import random, sys
from random import randint
import getopt

# This is where we define functions for each Biome. I have populated .txt files with the pokemon names I have a common, uncommon, and rare txt file for each biome type.


def cave_c():
	print(random.choice(list(open('biomes/cave_c.txt'))))
	return

def cave_uc():
	print(random.choice(list(open('biomes/cave_uc.txt'))))
	return

def cave_r():
	print(random.choice(list(open('biomes/cave_r.txt'))))	
	return

def forest_c():
	print(random.choice(list(open('biomes/forest_c.txt'))))
	return

def forest_uc():
	print(random.choice(list(open('biomes/forest_uc.txt'))))
	return

def forest_r():
	print(random.choice(list(open('biomes/forest_r.txt'))))
	return

def ghost_c():
	print(random.choice(list(open('biomes/ghost_c.txt'))))
	return

def ghost_uc():
	print(random.choice(list(open('biomes/ghost_uc.txt'))))
	return

def ghost_r():
	print(random.choice(list(open('biomes/ghost_r.txt'))))
	return

def grassland_c():
	print(random.choice(list(open('biomes/grassland_c.txt'))))
	return

def grassland_uc():
	print(random.choice(list(open('biomes/grassland_uc.txt'))))
	return
def grassland_r():
	print(random.choice(list(open('biomes/grassland_r.txt'))))
	return

def rough_c():
	print(random.choice(list(open('biomes/rough_c.txt'))))
	return

def rough_uc():
	print(random.choice(list(open('biomes/rough_uc.txt'))))
	return

def rough_r():
	print(random.choice(list(open('biomes/rough_r.txt'))))
	return

def sea_c():
	print(random.choice(list(open('biomes/sea_c.txt'))))
	return

def sea_uc():
	print(random.choice(list(open('biomes/sea_uc.txt'))))
	return

def sea_r():
	print(random.choice(list(open('biomes/sea_r.txt'))))
	return

def urban_c():
	print(random.choice(list(open('biomes/urban_c.txt'))))
	return

def urban_uc():
	print(random.choice(list(open('biomes/urban_uc.txt'))))
	return

def urban_r():
	print(random.choice(list(open('biomes/urban_r.txt'))))
	return

def wateredge_c():
	print(random.choice(list(open('biomes/wateredge_c.txt'))))
	return

def wateredge_uc():
	print(random.choice(list(open('biomes/wateredge_uc.txt'))))
	return

def wateredge_r():
	print(random.choice(list(open('biomes/wateredge_r.txt'))))
	return

def fossil():
	print(random.choice(list(open('biomes/fossil.txt'))))
	return

def industrial_c():
	print(random.choice(list(open('biomes/industrial_c.txt'))))
	return

def industrial_uc():
	print(random.choice(list(open('biomes/industrial_uc.txt'))))
	return

def industrial_r():
	print(random.choice(list(open('biomes/industrial_r.txt'))))
	return


# This is where we do a roll for rareness
rareness = randint(1,100)

# This is where we define Functions for an entire biome
# I want to see the roll, because if the pokemon does not fit into my current story I want to re-roll using the correct rarity, I don't want my party to miss out on a rare if it makes no sense to fight the particular rare that is chosen.


def cave():
	print rareness
	if rareness < 7:
		cave_r()
	elif rareness > 6 and rareness < 40:
		cave_uc()
	else:
		cave_c()
	return

def forest():
    print rareness
    if rareness < 7:
        forest_r()
    elif rareness > 6 and rareness < 40:
        forest_uc()
    else:
        forest_c()
    return

def ghost():
    print rareness
    if rareness < 7:
        ghost_r()
    elif rareness > 6 and rareness < 40:
        ghost_uc()
    else:
        ghost_c()
    return

def grassland():
    print rareness
    if rareness < 7:
        grassland_r()
    elif rareness > 6 and rareness < 40:
        grassland_uc()
    else:
        grassland_c()
    return

def industrial():
    print rareness
    if rareness < 7:
        industrial_r()
    elif rareness > 6 and rareness < 40:
        industrial_uc()
    else:
        industrial_c()
    return

def rough():
	print rareness
	if rareness < 7:
		rough_r()
	elif rareness > 6 and rareness < 40:
		rough_uc()
	else:
		rough_c()
	return

def sea():
    print rareness
    if rareness < 7:
        sea_r()
    elif rareness > 6 and rareness < 40:
        sea_uc()
    else:
        sea_c()
    return

def urban():
    print rareness
    if rareness < 7:
        urban_r()
    elif rareness > 6 and rareness < 40:
        urban_uc()
    else:
        urban_c()
    return

def wateredge():
    print rareness
    if rareness < 7:
        wateredge_r()
    elif rareness > 6 and rareness < 40:
        wateredge_uc()
    else:
        wateredge_c()
    return

#Now define usage for if you forget what you are supposed to type as a flag to make the things work

def usage():
	print "Please pass one of the following flags --cave_c, --cave_uc, --cave_r, --forest_c, --forest_uc, --forest_r, --fossil, --ghost_c, --ghost_uc, --ghost_r, --grassland_c, --grassland_uc, --grassland_r, --industrial_c, --industrial_uc, --industrial_r, --rough_c, --rough_uc, --rough_r, --sea_c, --sea_uc, --sea_r, --urban_c, --urban_uc, --urban_r, --wateredge_c, --wateredge_uc, --wateredge_r, --forest, --cave, --ghost, --grassland, --industrial, --rough, --sea, --urban, --wateredge"


# Here we actually start the program, testing to see if our argument is a valid one

try:
	opts, args = getopt.getopt(sys.argv[1:], 'a:b:c', ['cave_c', 'cave_uc', 'cave_r', 'forest_c', 'forest_uc', 'forest_r', 'fossil', 'ghost_c', 'ghost_uc', 'ghost_r', 'grassland_c', 'grassland_uc', 'grassland_r', 'industrial_c', 'industrial_uc', 'industrial_r', 'rough_c', 'rough_uc', 'rough_r', 'sea_c', 'sea_uc', 'sea_r', 'urban_c', 'urban_uc', 'urban_r', 'wateredge_c', 'wateredge_uc', 'wateredge_r', 'forest', 'cave', 'ghost', 'grassland', 'industrial', 'rough', 'sea', 'urban', 'wateredge' ])

except getopt.GetoptError:
	usage()
	sys.exit(2)

# Now that we have a valid argument we can do something with it

for opt, arg in opts:
	if opt in ('-a', '--cave_c'):
		cave_c()
	elif opt in ('--forest'):
		forest()
	elif opt in ('--ghost'):
		ghost()
	elif opt in ('--cave'):
		cave()
	elif opt in ('--grassland'):
		grassland()
	elif opt in ('--industrial'):
		industrial()
	elif opt in ('--rough'):
		rough()
	elif opt in ('--sea'):
		sea()
	elif opt in ('--urban'):
		urban()
	elif opt in ('--wateredge'):
		wateredge()
	elif opt in ('-b', '--cave_uc'):
		cave_uc()
	elif opt in ('-c', '--cave_r'):
		cave_r()
	elif opt in ('--forest_c'):
		forest_c()
	elif opt in ('--forest_uc'):
		forest_uc()
	elif opt in ('--forest_r'):
		forest_r()
	elif opt in ('--fossil'):
		fossil()
	elif opt in ('--ghost_c'):
		ghost_c()
	elif opt in ('--ghost_uc'):
		ghost_uc()
	elif opt in ('--ghost_r'):
		ghost_r()
	elif opt in ('--grassland_c'):
		grassland_c()
	elif opt in ('--grassland_uc'):
		grassland_uc()
	elif opt in ('--grassland_r'):
		grassland_r()
	elif opt in ('--industrial_c'):
		industrial_c()
	elif opt in ('--industrial_uc'):
		industrial_uc()
	elif opt in ('--industrial_r'):
		industrial_r()
	elif opt in ('--rough_c'):
		rough_c()
	elif opt in ('--rough_uc'):
		rough_uc()
	elif opt in ('--rough_r'):
		rough_r()
	elif opt in ('--sea_c'):
		sea_c()
	elif opt in ('--sea_uc'):
		sea_uc()
	elif opt in ('--sea_r'):
		sea_r()
	elif opt in ('--urban_c'):
		urban_c()
	elif opt in ('--urban_uc'):
		urban_uc()
	elif opt in ('--urban_r'):
		urban_r()
	elif opt in ('--wateredge_c'):
		wateredge_c()
	elif opt in ('--wateredge_uc'):
		wateredge_uc()
	elif opt in ('--wateredge_r'):
		wateredge_r()
	else:
		usage()
		sys.exit(2)



