# test for logic

import sys, operator, random

Base1 = sys.argv[1]
Base2 = sys.argv[2]
Base3 = sys.argv[3]
Base4 = sys.argv[4]	
Base5 = sys.argv[5]
Base6 = sys.argv[6]
Level = 10

#relation = {1: Base1, 2: Base2, 3: Base3, 4: Base4, 5: Base5, 6: Base6}

relation = [(1, int(Base1)), (2, int(Base2)), (3, int(Base3)), (4, int(Base4)), (5, int(Base5)), (6, int(Base6))]

#sorted_relation = sorted(relation.items(), key=operator.itemgetter(1))
def getKey(item):
	return item[1]

new_relation = sorted(relation, key=getKey)

sorted_relation = new_relation[::-1]

print "Starting Stat table\n", sorted_relation


def statup():
	StatPoint = Level-1
	while StatPoint > 0:
#		Stat = random.choice(sorted_relation)
		StatI = random.randrange(len(sorted_relation))
		print StatI
		Stat = sorted_relation[StatI]
		print Stat
		StatN = int(Stat[0])
		print StatN
		StatV = int(Stat[1])
		print StatV
		prevstat = StatI - 1
#		if StatI > 0:
#			print "error Stat is less than 0!"
#			continue
		if StatI == 0:
			print "Highest Stat"
			NewV = StatV + 1
			print NewV
			sorted_relation[StatN] = NewV
			StatPoint -= 1
			continue
		elif StatV > sorted_relation[prevstat]:
			print "Greater than base relation allows"
			continue
		elif StatV <= sorted_relation[prevstat]:
			print "Adding a point to", StatN
			NewV = StatV + 1
			print StatV
			print NewV
			sorted_relation[StatN] = NewV
			StatPoint -= 1
			continue


statup()

print "Ending Stat table\n", sorted_relation
