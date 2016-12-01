# quick and dirty test of taking sqlite query and putting it into a dict

import random, sys, sqlite3, getopt

mon = sys.argv[1]

mon = (mon,)

conn = sqlite3.connect('PTA')
c = conn.cursor()
c.execute('SELECT WeightClass, Size, BaseHP, BaseAtk, BaseDef, BaseSpAtk, BaseSpDef, BaseSpeed, Capabilities, Type1, Type2 FROM Pokemon where Name=?' , mon)

dictionary = {}

result = c.fetchone()

dictionary = {"WeightClass": result[0], "Size": result[1], "BaseHP": result[2], "BaseAtk": result[3]}

print dictionary
