# test for logic

import sys, operator, random, math

# Arguments:
#   1: Level
#   2: Biome

level = 10
biome = "Woods" #?

def getPokemon(biome):
  # This will be a DB call.  Hard-coded for now.
  pokemon = { "name":"Charmander",
              "nature":"",
              "baseStats":{ "HP":4,
                            "Atk":5,
                            "Def":4,
                            "SpAtk":6,
                            "SpDef":5,
                            "Spd":7 },
              "addedStats":{ "HP":0,
                             "Atk":0,
                             "Def":0,
                             "SpAtk":0,
                             "SpDef":0,
                             "Spd":0 } }
  return pokemon
#end getPokemon()

def getNature():
  # This will be a DB call.  Hard-coded for now.
  nature = { "name":"Hardy",
             "raise":"HP",
             "lower":"Atk",
             "likes":"",
             "dislikes":"Spicy" }
  return nature
#end getNature()

def naturalize(pokemon, nature):
  pokemon["nature"] = nature["name"];
  modUp = 2
  modDn = 2
  if ( nature["raise"] == "HP" ):
    modUp = 1
  #end if
  if ( nature["lower"] == "HP" ):
    modDn = 1
  #end if
  pokemon["baseStats"][nature["raise"]] += modUp
  pokemon["baseStats"][nature["lower"]] -= modDn
  return pokemon # Unsure whether this is necessary.  Function might operate on 'pokemon' memory space directly.  Really, naturalize() should be a method of a pokemon class.
#end naturalize()

def statPrint(stats):
  statNames=sorted(stats, key=stats.__getitem__)
  string=""
  for name in statNames:
    string += str(name) + str(stats[name]) + ", "
  #end for
  return string
#end def

def levelUp(pokemon, level):
  # Note: I don't care which stat is which for now.  I'll assign that later, according to baseRelation
  # Get a sorted list of stats - we need to allocate biggest first
  stats = sorted(pokemon["baseStats"].values(), reverse=True)
  baseStats = stats[:] #Make a copy, so we can refer to what the baseStats were
  points = level - 1

  # Add random amounts to stats, starting with highest, then lowest, then the rest
  for stat in (0, 5, 1, 2, 3):
    if ( points < 1 ):
      break
    #end if
    increment = random.randint(0,points)
    points -= increment
    stats[stat] += increment
  #end for
  stats[4] += points
  stats.sort()

  if ( len(set(stats)) < len(set(baseStats)) ):
    print "Base relation tie problems."
  #end if

  # Assign new stats to the Pokemon's attributes, by Base Relation
  # Sort stats in order of base-relation
  # Assign stats
  statOrder = sorted(pokemon["baseStats"], key=pokemon["baseStats"].__getitem__)
  for x in range(0,6):
    pokemon["addedStats"][statOrder[x]] = stats[x]
  #end for

  # Calculate max and min for stat[0]
  return pokemon
#end levelUp()


# Select a random pokemon from the DB, that can appear in this biome
pokemon = getPokemon(biome)

# Choose a random nature
nature = getNature()

# If we end up with a pokemon class, this should be a method call:
#   pokemon.naturalize(nature)
pokemon = naturalize(pokemon, nature)

# At this point we "know" the base relation
# pokemon.levelUp(level)
pokemon = levelUp(pokemon, level)

print "Name:   ", pokemon["name"]
print "Level:  ", level
print "Nature: ", nature["name"]
print "Base Stats:  ", statPrint(pokemon["baseStats"])
print "Added Stats: ", statPrint(pokemon["addedStats"])


