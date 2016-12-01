# This is a script to gen wild pokemon encounters for the Pokemon Tabletop Adventure game (PTA)
# This iteration includes all pokemon up to Omega Ruby/Saphire (NO WILD MEGALUTIONS)
# This was created and owned by Anders Nelson aka Phixia/Pecanos
# This script is licensed under the Apache 2.0 License http://www.apache.org/licenses/

# The sqlite database I am using is forked from https://github.com/PanoramicPanda/PTU-Basic-Database special thanks to PanoramicPanda

# Some of the more complex logic was contributed by Andrew Howard aka StafDehat I will try to notate where in the script he helped most. 

# Note: This is my first real attempt at working on a big/involved python project so please feel free to offer constructive criticism and also bear with me while I figure out the wonderful world of python and object oriented programming.

# First we are going to import some modules and classes we will need later.
import random, sys, sqlite3, getopt

# Gonna import my classes/modules here;
#from nature import Nature
#from monmods import GetNature
#from  monmods import Shiny
#from monmods import Rareroll

mon = "null"

level = sys.argv[2]

# roll for shiny
def Shiny():
# Note: Shiny chance for my game is 1:100 if you want to be true to the video game it is either 1:4000 or 1:8000 (older generations)
	shiny = random.randint(1,100)
	if shiny == 1:
		print "SHINY!"
	return shiny
# /end shiny

# roll for rareness
def Rareroll():
	rareness = random.randint(1,100)
	return rareness
# / end roll for rareness

# function to get a nature from DB
def GetNature():
	conn = sqlite3.connect('PTA')
	data = conn.execute('SELECT Name FROM Natures ORDER BY RANDOM() LIMIT 1')
	for row in data:
		nature = row[0]
	return nature


# Now that we have a function to pull a nature from the DB lets make a class to define natures
class Nature(object):
	conn = sqlite3.connect('PTA')
	ModUp = 2
	ModDown = 2
	def __init__(self,nature):
# I have to put strings that go into sqlite3 queries in () with a comma so we do that below;
		natname = (nature,)
		natdata = Nature.conn.execute('SELECT StatUp, StatDown FROM Natures where Name=?', natname) 
		self.name = nature
		for row in natdata:
			self.StatUp = row[0]
			self.StatDown = row[1]
		if self.StatUp == "HP":
			Nature.ModUp = 1
		if self.StatDown == "HP":
			Nature.ModDown = 1
	def __str__(self):
		return "Nature: {}\n+{} {}\n-{} {}".format(self.name, Nature.ModUp, self.StatUp, Nature.ModDown, self.StatDown)
# /end Nature

# a Class for pokemon (have not figured this out fully yet)

class Pokemon(object):
# All Pokemon have the following:
# A name (the kind of pokemon)
# 6 Stats HP, Atk, Def, SpAtk, SpDef, and Speed
# WeightClass and Size
# A list of Capabilities
# A type or 2 types
# A nature
	def __init__(self, mon):
		self.name = mon
		mon = (mon,)
		self.level = int(level)
		conn = sqlite3.connect('PTA')
		data = conn.execute('SELECT WeightClass, Size, BaseHP, BaseAtk, BaseDef, BaseSpAtk, BaseSpDef, BaseSpeed,Capabilities, Type1, Type2 FROM Pokemon where Name=?' , mon)
		self.nature = GetNature()
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
		self.Type1 = (self.Type1 ,)
		self.Type2 = (self.Type2 ,)
		Typedata = conn.execute('SELECT Type from Types where TypeID =?', self.Type1)
		for i in Typedata:
			self.Type1 = i[0]
		Typedata = conn.execute('SELECT Type from Types where TypeID =?', self.Type2)
		for i in Typedata:
			self.Type2 = i[0]
	def __str__(self):
		return "{}\n{}\nHP: {}\nAtk: {}\nDef: {}\nSpAtk: {}\nSpDef: {}\nSpeed: {}\nType: {}/{}\nWeightClass: {}\nSize: {}\nCapabilities {}".format(self.name, Nature(self.nature), self.HP, self.Atk, self.Def, self.SpAtk, self.SpDef, self.Speed, self.Type1, self.Type2, self.WeightClass, self.Size, self.Capabilities)


# Now that we have a mon lets make some functions to do stuff with it's data

# Function to change base stats based on nature

	def Naturalize(self):
		# First we grab the nature from our pokemon object and get the object for that nature
		nature = Nature(self.nature)
		BaseStats = {"BaseHP": self.HP, "BaseAtk": self.Atk, "BaseDef": self.Def, "BaseSpAtk": self.SpAtk, "BaseSpDef": self.SpDef, "BaseSpeed": self.Speed}
		StatPoint = self.level - 1
		NewStats = {"HP": self.HP, "Atk": self.Atk, "Def": self.Def, "SpAtk": self.SpAtk, "SpDef": self.SpDef, "Speed": self.Speed}
		NewStats[nature.StatUp] = self.(nature.Statup) += nature.ModUp
		NewStats[nature.StatDown] = self.%s %nature.StatDown -= nature.ModDown
		
#			while Statpoint > 0
			
		return BaseStats




#		BaseHP = self.HP
#		BaseAtk = self.Atk
#		BaseDef = self.Def
#		BaseSpAtk = self.SpAtk
#		BaseSpDef = self.SpDef
#		BaseSpeed = self.Speed	

		
		# Then we call the DB to get the StatUp and StatDown for that nature
#		natdata = conn.execute('SELECT StatUp, StatDown FROM Natures where Name=?', nature)
#		for i in natdata:
#			StatUp = i[0]
#			StatDown = i[1]



	# This is a list of all what we want to do with our object Pokemon
	# gonna need a function to take a nature and alter the base stats
	# gonna need a function to take the nature altered base stats and level the pokemon n levels while keeping base relation
	# gonna need a function to grab all the moves a mon can learn
	# add a function to pull the info for a move (probably a different python program specifically for this is a better idea)




# /end Pokemon		



# Before we do anything we need to grab a random pokemon from a biome

class Biome(object):
#All Biomes have the following:
#		3 .txt files with lists of pokemon for common pokemon Biome_c.txt, uncommon pokemon Biome_uc.txt, and rare pokemon Biome_r.txt
#		All biomes will be used to generate random pokemon from these three files based on a d100 roll
#		All biomes will also do a d100 roll to determine if the generated pokemon is shiny or not

	def __init__(self, name):
# create a Biome object whose name is *name*.
		self.name = name

# define function to pull a common mon from a biome
	def common(self):
		self.f = open('biomes/%s_c.txt' %self.name)
		self.mons = self.f.read().splitlines()
		self.mon = random.choice(self.mons)
		return self.mon
# /end common
# define function to pull uncommon mon from a biome	
	def uncommon(self):
		self.f= open('biomes/%s_c.txt' %self.name)
		self.mons = self.f.read().splitlines()
		self.mon = random.choice(self.mons)
		return self.mon
# /end uncommon
# define function to pull a rare mon from a biome
	def rare(self):	
		self.f = open('biomes/%s_c.txt' %self.name)
		self.mons = self.f.read().splitlines()
		self.mon = random.choice(self.mons)
		return self.mon
# /end rare

# define the funciton to actually gen a random mon I also want this to give the mon a nature, alter the base stats to that nature and then print the new basestats and assign stat points based on a level that I pass to the script. I would like to use this function elsewhere so I will probably build a class/function and import it here.


	def encounter(self):
		Shiny()
		rareness = Rareroll()
		if rareness < 6:
			self.rare()	
			return self.mon 
		if rareness > 5 and rareness < 41:
			self.uncommon()
			return self.mon
		else:
			self.common()
			return self.mon 

# /end Biome object

# Now we use all the stuff we made below we say; take the first argument passed by CLI when we call the script and use it as the biome name, then we will gen a pokemon for that biome and pull the base info for it.
biome = Biome(str(sys.argv[1]))

pokemon = Pokemon(biome.encounter())
#print pokemon

x = Pokemon("Geodude")
y = x.Naturalize()

print y


