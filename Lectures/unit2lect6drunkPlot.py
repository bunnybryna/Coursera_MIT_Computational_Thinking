import random, pylab
pylab.rcParams['lines.linewidth']=4
pylab.rcParams['axes.titlesize']=20
pylab.rcParams['axes.labelsize']=20
pylab.rcParams['xtick.labelsize']=16
pylab.rcParams['ytick.labelsize']=16
pylab.rcParams['xtick.major.size']=7
pylab.rcParams['ytick.major.size']=7
pylab.rcParams['legend.numpoints']=1

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
	


#random.seed(0)
#simAll((UsualDrunk, ColdDrunk),(1,10,100,1000,10000),100)

# styleChoice=styleIterator(('m-','b--','g-.'))
# styles = ('m-','b--','g-.'),a tuple, that's why double layer () 
# since len(styles) = 3
# curStyle = nextStyle will iterate through this ring structor from index 0 to 2 then back to 0

class styleIterator(object):
	def __init__(self, styles):
		self.index = 0
		self.styles = styles
		
	def nextStyle(self):
		result = self.styles[self.index]
		# when move to the end, start over again
		if self.index == len(self.styles) - 1:
			self.index = 0
		# move to next index
		else:
			self.index += 1
		return result

def simDrunk(numTrials, dClass, walkLengths):
	meanDistance = []
	for numSteps in walkLengths:
		print('Starting simpulation of', numSteps, 'steps')
		trials = simWalks(numSteps, numTrials, dClass)
		mean = sum(trials)/len(trials)
		meanDistance.append(mean)
	return meanDistance

# def simAll(drunkKinds, walkLengths, numTrials):
	# for dClass in drunkKinds:
		# drunkTest(walkLengths, numTrials, dClass)	
def simAll(drunkKinds, walkLengths, numTrials):
	styleChoice = styleIterator(('m-','b--','g-.'))
	for dClass in drunkKinds:
		curStyle = styleChoice.nextStyle()
		print('Starting simulation of ',dClass.__name__)
		means = simDrunk(numTrials, dClass, walkLengths)
		pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
		pylab.title('Mean Distance from Origin(' + str(numTrials)+'trials)')
		pylab.xlabel('Numer of Steps')
		pylab.ylabel('Distance from Origin')
		pylab.legend(loc = 'best')
		
# random.seed(0)
# numSteps = (10,100,1000,10000)
# simAll((UsualDrunk, ColdDrunk), numSteps, 100)

def getFinalLocs(numSteps, numTrials, dClass):
	locs = []
	d = dClass()
	for t in range(numTrials):
		f = Field()
		f.addDrunk(d, Location(0,0))
		for s in range(numSteps):
			f.moveDrunk(d)
		locs.append(f.getLoc(d))
	return locs

def plotLocs(drunkKinds, numSteps, numTrials):
	styleChoice = styleIterator(('k+','r^','mo'))
	for dClass in drunkKinds:
		locs = getFinalLocs(numSteps, numTrials, dClass)
		xVals, yVals = [],[]
		for loc in locs:
			xVals.append(loc.getX())
			yVals.append(loc.getY())
		xVals = pylab.array(xVals)
		yVals = pylab.array(yVals)
		meanX = sum(abs(xVals))/len(xVals)
		meanY = sum(abs(xVals))/len(xVals)
		curStyle = styleChoice.nextStyle()
		pylab.plot(xVals, yVals, curStyle, label = dClass.__name__+'mean abs dist = <'+str(meanX)+','+str(meanY)+'>')
	pylab.title('Location at End of Walks ('+str(numSteps)+' steps')
	pylab.ylim(-1000,1000)
	pylab.xlim(-1000,1000)
	pylab.xlabel('Steps East/West of Origin')
	pylab.ylabel('Steps North/South of Origin')
	pylab.legend(loc = 'upper left')

# random.seed(0)
# plotLocs((UsualDrunk, ColdDrunk), 1000, 1000)

class OddField(Field):
	def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
		Field.__init__(self)
		self.wormholes = {}
		for w in range(numHoles):
			x = random.randint(-xRange, xRange)
			y = random.randint(-yRange, yRange)
			newX = random.randint(-xRange, xRange)
			newY = random.randint(-yRange, yRange)
			newLoc = Location(newX, newY)
			self.wormholes[(x,y)]=newLoc
			
		def moveDrunk(self, drunk):
			Field.moveDrunk(self,drunk)
			x = self.drunks[drunk].getX()
			y = self.drunks[drunk].getY()
			if (x, y) in self.wormholes:
				self.drunks[drunk] = self.wormholes[(x,y)]
			
			
def traceWalk(fieldKinds, numSteps):
	styleChoice = styleIterator(('b+','r^','ko'))
	for fClass in fieldKinds:
		d = UsualDrunk()
		f = fClass()
		f.addDrunk(d, Location(0,0))
		locs = []
		for s in range(numSteps):
			f.moveDrunk(d)
			locs.append(f.getLoc(d))
		xVals, yVals = [],[]
		for loc in locs:
			xVals.append(loc.getX())
			yVals.append(loc.getY())
		curStyle = styleChoice.nextStyle()
		pylab.plot(xVals, yVals, curStyle, label = fClass.__name__)
	pylab.title('Spots Visited on Walk ('+str(numSteps) + ' steps')
	pylab.xlabel('Steps East/West of Origin')
	pylab.ylabel('Steps North/South of Origin')
	pylab.legend(loc = 'best')

random.seed(0)
traceWalk((Field, OddField), 500)