import random, sys, sqlite3, getopt
sys.path.insert(0, "modules/")
from collections import Counter
from monmods import Shiny
from monmods import RareRoll
from nature import Nature
class Pokemon(object):
# All Pokemon have the following:
# A name (the kind of pokemon)
# 6 Stats HP, Atk, Def, SpAtk, SpDef, and Speed
# WeightClass and Size
# A list of Capabilities
# A type or 2 types
# A nature
# An Ability
# A sex (Maybe!)

	def __init__(self, mon, level):
		self.name = mon
		mon = (mon,)
		self.level = int(level)
		self.nature = GetNature()
# Come back and clean up the DB stuff by making it into a method that __init__ can just call.

		conn = sqlite3.connect('PTA')
		data = conn.execute('SELECT WeightClass, Size, BaseHP, BaseAtk, BaseDef, BaseSpAtk, BaseSpDef, BaseSpeed,Capabilities, Type1, Type2, Number, Male, Female FROM Pokemon where Name=?' , mon)
		for row in data:
			self.WeightClass = row[0]
			self.Size = row[1]
			self.HP = row[2]
			self.Atk = row[3]
			self.Def = row[4]
			self.SpAtk = row[5]
			self.SpDef = row[6]
			self.Speed = row[7]
			self.Type1 = row[9]
			self.Type2 = row[10]
			self.Capabilities = row[8]
			self.num = row[11]
			self.Mchance = int(row[12])
			self.Fchance = int(row[13])
		self.Naturalize(Nature())
		self.Type1 = (self.Type1 ,)
		self.Type2 = (self.Type2 ,)
		Typedata = conn.execute('SELECT Type from Types where TypeID =?', self.Type1)
		for i in Typedata:
			self.Type1 = i[0]
		Typedata = conn.execute('SELECT Type from Types where TypeID =?', self.Type2)
		for i in Typedata:
			self.Type2 = i[0]

### /end DB call for Basestats

		self.BaseStats = {"HP": int(self.HP), "Atk": int(self.Atk), "Def": int(self.Def), "SpAtk": int(self.SpAtk), "SpDef": int(self.SpDef), "Speed": int(self.Speed)}




### This could also be its own method that gets ability information
# I will likely leave this for now as the abilities in the DB are currently for PTU and thus moot for me.

		self.num = (self.num ,)
		abilitydata = conn.execute('SELECT AbilityID From PokemonAbilities WHERE PokemonNum=? and AbilityLevel=1 ORDER BY RANDOM() LIMIT 1' , self.num)
		for i in abilitydata.fetchall():
			ability = i
		abilitydata2 = conn.execute('SELECT Name from Abilities WHERE AbilityID=?' , ability)	
		for i in abilitydata2:
			self.Ability = i[0]

# This is the function to print out our Pokemon Object so whatever we define here we will see when we run stuff.

	def __str__(self):
		output = ( "{}\n"
							"{}\n"
							"Ability: {}\n"
							"HP: {}\n"
							"Atk: {}\n"
							"Def: {}\n"
							"SpAtk: {}\n"
							"SpDef: {}\n"
							"Speed: {}\n"
							"Type: {}/{}\n"
							"WeightClass: {}\n"
							"Size: {}\n"
							"Sex: {}\n"
							"Capabilities {}" )
		return output.format(self.name,
									self.nature.name,
									self.Ability,
									self.HP,
									self.Atk,
									self.Def,
									self.SpAtk,
									self.SpDef,
									self.Speed,
									self.Type1,
									self.Type2,
									self.WeightClass,
									self.Size,
									self.Sex(),
									self.Capabilities )




# Now that we have a mon lets make some functions to do stuff with it's data


	def Sex(self):
		if self.Mchance == 0 and self.Fchance == 0:
			sex = 'N/A' 
		elif RareRoll() <= int(self.Mchance):
			sex = 'M'
		else:
			sex = 'F'
		return sex

	def Naturalize(self, nature):
		modded = collections.Counter(self.BaseStats)
		modded.update(nature.statMods)
		self.BaseStats = dict(modded)
		self.nature = nature
	
	def LevelUp(self):
		StatPoints = self.level - 1
		Stats = sorted(self.BaseStats.values(), reverse=True)
		BaseStats = Stats[:]
		Newstats = {}
	
		for i in (0,5,1,2,3):
			if StatPoints < 1:
				break
			Increment = random.randint(0,StatPoints)
			StatPoints -= Increment
			Stats[i] += Increment
			Stats[4] += StatPoints
			Stats.sort()

			if ( len(set(Stats)) < len(set(BaseStats)) ):
				print "Base relation tie problems"

		StatOrder = sorted(self.BaseStats.keys())
		for x in range(0,6):
			Newstats[StatOrder[x]] = Stats[x]

		return Newstats	

