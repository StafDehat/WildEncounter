import random, sys, sqlite3, getopt

# roll for shiny
def shiny():
# Note: Shiny chance for my game is 1:100 if you want to be true to the video game it is either 1:4000 or 1:8000 (older generations)
	shiny = randint(1,100)
	if shiny == 1:
		print "SHINY!"
	return shiny
# /end shiny

# roll for rareness
def rareroll():
	rareness = randint(1,100)
	return rareness
# / end roll for rareness


# Before we do anything we need to grab a random pokemon from a biome

class Biome(object):
#All Biomes have the following:
#		3 .txt files with lists of pokemon for common pokemon Biome_c.txt, uncommon pokemon Biome_uc.txt, and rare pokemon Biome_r.txt
#		All biomes will be used to generate random pokemon from these three files based on a d100 roll
#		All biomes will also do a d100 roll to determine if the generated pokemon is shiny or not

	def __init__(self, name):
# create a Biome object whose name is *name*.
		self.name = name
	def test(self):
		print self.name
		return

	def common(self):
		f = open('biomes/%s_c.txt' %self.name)
		mons = f.read().splitlines()
		mon = random.choice(mons)
		mon = (mon,)
		return mon
	
	def uncommon(self):
		f= open('biomes/%s_c.txt' %self.name)
		mons = f.read().splitlines()
		mon = random.choice(mons)
		mon = (mon,)
		return mon

	def rare(self):	
		f = open('biomes/%s_c.txt' %self.name)
		mons = f.read().splitlines()
		mon = random.choice(mons)
		mon = (mon,)
		return mon

	def encounter(self):
		print self.name
		shiny()
		rareroll()
		if rareness < 6:
			rare(self)	
			print mon
		if rareness > 5 and rareness < 41:
			uncommon(self)
			print mon
		else:
			common(self)
			print mon
		return mon

# /end Biome object

grassland = Biome("grassland")

grassland.test
