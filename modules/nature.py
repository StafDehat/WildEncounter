import random, sys, sqlite3, getopt
sys.path.insert(0, "modules/")
from collections import Counter
from monmods import Shiny
from monmods import RareRoll

class Nature(object):
	conn = sqlite3.connect('PTA')
	ModUp = 2
	ModDown = 2
	def __init__(self,name="random"):
# I have to put strings that go into sqlite3 queries in () with a comma so we do that below;
		# If no nature specified, pick one randomly
		if ( name == "random" ):
			data = conn.execute('SELECT Name FROM Natures ORDER BY RANDOM() LIMIT 1')
			name = data[0][0]
		#end if
		natname = (nature,)
		natdata = Nature.conn.execute('SELECT Name, StatUp, StatDown, Likes, Dislikes FROM Natures where Name=?', natname)
		self.name = natdata[0][0]
		self.StatUp = natdata[0][1]
		self.StatDown = natdata[0][2]

		if self.StatUp == "HP":
			self.ModUp = 1
		if self.StatDown == "HP":
			self.ModDown = 1

		self.StatMods = {str(self.StatUp): int(Nature.ModUp),
							  str(self.StatDown): int(Nature.ModDown)}
	def __str__(self):
		output = "Nature: {}\n+{} {}\n-{} {}"
		return output.format(self.name,
									self.ModUp,
									self.StatUp,
									self.ModDown,
									self.StatDown)
