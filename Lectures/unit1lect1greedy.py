'''optimization model
1. an objective function that is to be maxmized or minimized
2. a set of constraints (possibly empty)
=> approximate solution that is good enough

Knapsack Problem
1. 0/1 knapsack problem, one or not at all(harder)
2. continuous or fractional knapsack problem'''

class Food(object):
	def __init__(self, n, v, w):
		self.name = n
		self.value = v
		self.calories = w
	def getValue(self):
		return self.value
	def getCost(self):
		return self.calories
	def density(self):
		return self.getValue()/self.getCost()
	def __str__(self):
		return self.name + ': <' +str(self.value)+' ,' + str(self.calories) + '>'

def buildMenu(names, values, calories):
	menu = []
	for i in range(len(values)):
		menu.append(Food(names[i],values[i],calories[i]))
	return menu

#keyFunction makes our implementation independent of the definition of best
def greedy(items, maxCost, keyFunction):
#sorted() function returns a new sorted list while sort() just sort the list
	itemsCopy = sorted(items, key = keyFunction, reverse = True)
	result = []
	totalValue, totalCost = 0.0, 0.0
	for i in range(len(itemsCopy)):
		if (totalCost+itemsCopy[i].getCost()) <= maxCost:
			result.append(itemsCopy[i])
			totalCost += itemsCopy[i].getCost()
			totalValue += itemsCopy[i].getValue()
	return (result, totalValue)
	
def testGreedy(items, constraint, keyFunction):
	taken, val = greedy(items, constraint, keyFunction)
	print('Total value of items taken =', val)
	for item in taken:
		print (' ', item)

def testGreedys(foods, maxUnits):
	print('Use greedy by value to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.getValue)
	
	print('\nUse greedy by cost to allocate', maxUnits, 'calories')
	# an expression
	# lambda <id1, id2,... idn>:<expression>
	testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
	
	print('\nUse greedy by density to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)

# why different answers? local optimum
# 1000=> value, 750=> cost and density
# lambda 
'''
f1 = lambda x:x

f1(3)
Out[2]: 3

f1('a')
Out[3]: 'a'

f2 = lambda x,y : x+y

f2(2,3)
Out[5]: 5

f2('a','b')
Out[6]: 'ab'

f3 = lambda x,y : 'factor' if (x%y == 0) else 'not factor'

f3(4,2)
Out[8]: 'factor'

f3(4,3)
Out[9]: 'not factor'
'''