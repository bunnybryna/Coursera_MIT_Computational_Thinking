###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # sort a copy of the dictionary
    cowsCopy = cows
    # lambda's just like using a named function
	# def element1(x):
		#return x[1]	
	# .items() returns (key, value) pairs
	# we use x[1] which is the value to sort
	# cowsPair is a list of pairs with descending value 
    cowsPair = sorted(cowsCopy.items(),key=lambda x:x[1], reverse = True)
    listOfTrips = []
	# iterate the sorted pairs to fit trips	
    while len(cowsPair) != 0:
        oneTrip = []
        limitOfTrip = limit
        for pairs in cowsPair:
            if pairs[1] <= limitOfTrip:
                oneTrip.append(pairs[0])
                limitOfTrip = limitOfTrip-pairs[1]
                cowsPair.remove(pairs)
        listOfTrips.append(oneTrip)
    return listOfTrips

    


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # get partition from helper function
    cowsCopy = cows
    keyList = sorted(cowsCopy, key=cowsCopy.get)
    lenmin = None
    tripmin = None
    for partition in get_partitions(keyList):
        flag = True
        for oneTrip in partition:
            total = 0
            for name in oneTrip:
                total += cowsCopy[name]
            if total > limit:
                flag = False
                break	
            else: 
                continue
        if flag and (lenmin == None or lenmin > len(partition)):	
            lenmin = len(partition)
            tripmin = partition    
    return tripmin

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    limit = 10
    cows = load_cows("ps1_cow_data.txt")
    startGreedy = time.time()
    print(greedy_cow_transport(cows, limit))
    endGreedy = time.time()
    timeGreedy = endGreedy - startGreedy
    startBF = time.time()
    print(brute_force_cow_transport(cows, limit))
    endBF = time.time()
    timeBF = endBF - startBF
    print ('Greedy is ', timeGreedy, 'Brute Force is ', timeBF)



"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""
#cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
#print(greedy_cow_transport(cows, limit))
#cows = load_cows("ps1_cow_data.txt")
# limit=100
# print(cows)

# print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, 10))

compare_cow_transport_algorithms()


