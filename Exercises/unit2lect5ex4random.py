import random
# same both 
if the first random number is >0.5:
    generate and return another random numer in range (0,1)
# this range is [-1,1)
def dist1():
    return random.random() * 2 - 1

# togehter, this range is [-1,1) 
def dist2():
    if random.random() > 0.5:
	# it invokes random.random() second time, its range[0,1) 
        return random.random()
	# its range [-1,0)
    else:
        return random.random() - 1 
		
# same both [0,10)
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

# different,
# this range is [0,10) since random.random()range is [0,1)
def dist5():
    return int(random.random() * 10)
# this range is [0,10]
def dist6():
    return random.randint(0, 10)	