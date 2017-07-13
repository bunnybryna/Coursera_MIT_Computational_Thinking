import random

class Location(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def move(self, deltaX, deltaY):
		return Location(self.x+deltaX, self.y+deltaY)
		
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
		
	def distFrom(self, other):
		ox = other.x
		oy = other.y
		xDist = self.x - ox
		yDist = self.y - oy
		return (xDist**2 + yDist**2)**0.5
		
	def __str__(self):
		return '<'+str(self.x)+','+str(self.y)+'>'
		
# a field is a mapping from drunks to locations		
class Field(object):
	def __init__(self):
		self.drunks = {}
	# the key design decision here is to make the location of a drunk in a field an attribute of the field rather than an attribute of the drunk
	# it allows to think how drunks relate to one anohter spatially
	def addDrunk(self, drunk, loc):
		if drunk in self.drunks:
			raise ValueError('Duplicate drunk')
		else:
			self.drunks[drunk]=loc
	def moveDrunk(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		xDist, yDist = drunk.takeStep()
		currentLocation = self.drunks[drunk]
		self.drunks[drunk] = currentLocation.move(xDist, yDist)
	
	def getLoc(self, drunk):
	# defensive programming
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		return self.drunks[drunk]

# this class is not intended to be useful on its own
# it's a base class to be inherited		
class Drunk(object):
	def __init__(self, name = None):
		self.name = name
	def __str__(self):
		if self!= None:
			return self.name
		return 'Anonymouse'

class UsualDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0,1),(0,-1),(1,0),(-1,0)]
		return random.choice(stepChoices)
		
class ColdDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0.0,0.9),(0.0,-1.1),(1.0,0.0),(-1.0,0.0)]
		return random.choice(stepChoices)

# f a Field, d a Drunk in f
# returns the distance between from and to		
def walk(f, d, numSteps):
	start = f.getLoc(d)
	for s in range(numSteps):
		f.moveDrunk(d)
	return start.distFrom(f.getLoc(d))
	
def simWalks(numSteps, numTrials, dClass):
	Homer = dClass()
	origin = Location(0,0)
	distances = []
	for t in range(numTrials):
		f = Field()
		f.addDrunk(Homer, origin)
		distances. append(round(walk(f, Homer, numSteps),1))
	return distances

#print(simWalks(5,6,ColdDrunk))
def drunkTest(walkLengths, numTrials, dClass):
	for numSteps in walkLengths:
		distances = simWalks(numSteps, numTrials, dClass)
		print(dClass.__name__,' random walk of ', numSteps, ' steps')
		print('Mean = ', round(sum(distances)/len(distances),4))
		print('Max = ',max(distances), ' Min = ', min(distances))
		
# random.seed(0)
# drunkTest((10,100,1000,10000),100,UsualDrunk)
	
def simAll(drunkKinds, walkLengths, numTrials):
	for dClass in drunkKinds:
		drunkTest(walkLengths, numTrials, dClass)

random.seed(0)
simAll((UsualDrunk, ColdDrunk),(1,10,100,1000,10000),100)