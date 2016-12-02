import random, sys, sqlite3

def Shiny():
	# Note: Shiny chance for my game is 1:100 if you want to be true to the video game it is either 1:4000 or 1:8000 (older generations)
	shiny = random.randint(1,100)
	if shiny == 1:
		print "SHINY!"
	return shiny
# /end shiny

def RareRoll():
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
