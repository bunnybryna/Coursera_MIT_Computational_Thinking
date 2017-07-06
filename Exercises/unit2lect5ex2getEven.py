import random
#random.randint(1, 5)
#random.choice(['apple', 'banana', 'cat'])

def genEven():
#Returns a random number x, where 0 <= x < 100
	evenList = []
	for i in range(0,100):
		if i%2 == 0:
			evenList.append(i)
	return random.choice(evenList)
	
def deterministicNumber():
#Deterministically generates and returns an even number between 9 and 21
	return 20
	
def stochasticNumber():
# Stochastically generates and returns a uniformly distributed even number between 9 and 21
    evenList = []
	for i in range(10,22,2)
		evenList.append(i)
	return random.choice(evenList)
