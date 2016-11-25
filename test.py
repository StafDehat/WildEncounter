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

def levelUp(pokemon, level):
  # Note: I don't care which stat is which for now.  I'll assign that later, according to baseRelation
  # Get a sorted list of stats - we need to allocate biggest first
  stats = sorted(pokemon["baseStats"].values(), reverse=True)
  baseStats = stats[:] #Make a copy, so we can refer to what the baseStats were

  #Note: Ties are fucking this up.
  # If 2x stats are tied, they have to relation relative to each other - only the things actually > or < themselves.
  points = level - 1

  for thisStat in range(0,5):
    myMinPts=0
    myMaxPts=0
    statsToGo = 5-thisStat

    #
    # Find MAX
    # Initial assumption - maybe I'm the biggest stat
    myMaxPts = points
    # For each stat to my left, look for someone who caps me
    for x in range(thisStat-1, -1, -1):
      if ( baseStats[thisStat] < baseStats[x] ):
        # My max is 1 less than his current
        myMaxPts = max( ( stats[x] - 1 ) - baseStats[thisStat], 0)
        break
      #end if
      # Else, I was tied with him.  He doesn't rule me.
    #end for


    #
    # Find MIN
    # Assuming we don't change this one at all, how many stats can we burn in the remaining slots?
    burnable = 0
    # Start from right (ie:smallest).
    # Increment 'til it almost ties its left neighbour.
    for x in range(5,thisStat,-1):
      # For each stat right of thisStat, find its limiter
      limiter = 0
      for y in range(x-1, 0, -1):
        if ( baseStats[y] > baseStats[x] ):
          #Not a tie, so baseStats[y]-1 is an upper cap on baseStats[x]
          limiter = y
        #end if
      #end for y
      # Increment this guy and his lessers, until he's capped by limiter
      burnable += max( ( baseStats[limiter] - 1 - baseStats[x] ) * ( 6 - x ), 0 )
    #end for

    # And that leaves X points left-over, which, when distributed "evenly" among
    #   all stats, keeps *this* stat at its minimum possible value.
    myMinPts = math.ceil( (points-burnable) / (statsToGo+1) )


    #
    # Choose a random value between myMaxPts and myMinPts, for this stat.
    myPts = random.randint(myMinPts, myMaxPts)
    myVal = baseStats[thisStat] + myPts

    # Update the stats lists
    stats[thisStat] = myVal

    # Update counters
    points -= myPts
    thisStat += 1
    statsToGo -= 1
  #end while

  # Assign new stats to the Pokemon's attributes, by Base Relation
  # Sort stats in order of base-relation
  # Assign stats

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
print "Base Stats: ", pokemon["baseStats"]
print "Added Stats: ", pokemon["addedStats"]


