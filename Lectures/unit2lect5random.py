import random

def rollDie():
	return random.choice([1,2,3,4,5,6])
	
def testRoll(n=10):
	result = ''
	for i in range(n):
		result = result + str(rollDie())
	print(result)
	
testRoll(5)