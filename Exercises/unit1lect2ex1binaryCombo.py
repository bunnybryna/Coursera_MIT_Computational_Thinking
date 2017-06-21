# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:15:00 2017

@author: bryna
if N=8
d8    d7    d6    d5    d4    d3    d2    d1
(pizza cheese apple water juice meat egg rice)
0     0     0     0     0      0      0     0
0     0     0     0     0      0      0     1
0     0     0     0     0      0      1     0
0     0     0     0     0      0      1     1
0     0     0     0     0      1      0     0
0     0     0     0     0      1      0     1
..
..
..
1     1     1     1     1      1      1     1
The code make use of this similarity between binary numbers and the idea of the number of combinations. 
So, if we have N items, we could have 2**N different combinations,
we can also represent each combination using a different binary number represented in N digits.
1 means that we will take that item, 0 means that we won't take it. 
"""
# use s=Powerset(items) and s.__next__() to call
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
		
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
	N = len(items)
	for i in range(3**N):
		bag1 = []
		bag2 = []        
		for j in range(N):
			if (i // (3 ** j))%3 == 1:
				bag1.append(items[j])
			if (i // (3 ** j))%3 == 2: 
				bag2.append(items[j])
		yield (bag1, bag2)