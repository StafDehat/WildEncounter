# This script will stat out a pokemon based on 3 vairables entered by they user
# Pokemon (To grab the base stats for that mon), # Nature (To change the base stats according to nature), Level (To determine the number of stat points the script will apply)

import random, sys, sqlite3, getopt


# First lets set default values for each Variable then lets capture the variables from the CLI

mon = str(sys.argv[1])
nature = str(sys.argv[2])
level = int(sys.argv[3])

mon = (mon ,)
nature = (nature ,)



def basestats(mon, nature):
	conn = sqlite3.connect('PTA')
	data = conn.execute('SELECT BaseHP, BaseAtk, BaseDef, BaseSpAtk, BaseSpDef, BaseSpeed FROM Pokemon where Name=?' , mon)
	for row in data:
		BaseHP = row[0]
		BaseAtk = row[1]
		BaseDef = row[2]
		BaseSpAtk = row[3]
		BaseSpDef = row[4]
		BaseSpeed = row[5]
	

	print "Initial BaseStats"
	print "HP=" ,BaseHP
	print "Atk=",BaseAtk
	print "Def=",BaseDef
	print "SpAtk=",BaseSpAtk
	print "SpDef=",BaseSpDef
	print "Speed=",BaseSpeed

	natdata = conn.execute('SELECT StatUp, StatDown FROM Natures where Name=?', nature)
	for i in natdata:
		StatUp = i[0]
		StatDown = i[1]
	if StatUp == 'HP':
		BaseHP +=1
	elif StatUp == 'Atk':
		BaseAtk +=2
	elif StatUp == 'Def':
		BaseDef +=2
	elif StatUp == 'SpAtk':
		BaseSpAtk +=2
	elif StatUp == 'SpDef':
		BaseSpDef +=2
	elif StatUp == 'Speed':
		BaseSpeed +=2
	else:
		print "Error with StatUp"	

	if StatDown == 'HP':
		BaseHP -=1
	elif StatDown == 'Atk':
		BaseAtk -=2
	elif StatDown == 'Def':
		BaseDef -=2
	elif StatDown == 'SpAtk':
		BaseSpAtk -=2
	elif StatDown == 'SpDef':
		BaseSpDef -=2
	elif StatDown == 'Speed':
		BaseSpeed -=2
	else:
		print "Error with StatDown"

	print "BaseStats after Nature"
	print "Hp=",BaseHP
	print "Atk=",BaseAtk
	print "Def=",BaseDef
	print "SpAtk=",BaseSpAtk
	print "SpDef=",BaseSpDef
	print "Speed=",BaseSpeed


basestats(mon, nature)

	


#def statmon(mon, nature, level):
#	statpoint = level - 1
	



