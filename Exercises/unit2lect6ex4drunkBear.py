'''Suppose we wanted to create a class PolarBearDrunk, a drunk polar bear who moves randomly along the x and y axes taking large steps when moving South, and small steps when moving North.'''

class PolarBearDrunk(Drunk):
    def takeStep(self):
        # code for takeStep()

# return a tuple of length of 4
directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0)]
myDirection = random.choice(directionList)
if myDirection[0] == 0.0:
# should be return (myDirection[0], myDirection[1] - 0.5) 
    return myDirection + (0.0, -0.5)
return myDirection

# incorrect because it produces directions not along axes
# only North/South move should be changed
directionList = [(0.0, 0.5), (1.0, -0.5), (-1.0, -0.5), (0.0, -1.5)]
return random.choice(directionList)

# correct
directionList = [(0.0, 0.5), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.5)]
return random.choice(directionList)

# incorrect because it produces a bias toward moving South, but does not alter step size
directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (0.0, -1.0)]
return random.choice(directionList)