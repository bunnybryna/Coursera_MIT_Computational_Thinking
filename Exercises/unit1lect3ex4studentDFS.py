'''We saw before that for permutations of 3 people in line, any two nodes are at most three edges, or four nodes, away. But DFS has yielded paths longer than three edges! In this graph, given a random source and a random destination, what is the probability of DFS finding a path of the shortest possible length?
1- If the dest. is the node itself, DFS will get the shortest path by prob. of 100%.

2- If the dest. is one node away, DFS will get the shortest path by prob. of 50% (because it may rotate to the other direction).

3- If the dest. is two nodes away, DFS will get the shortest path also by prob. of 50% (because it may rotate to the other direction).

4- If the dest. is three nodes away, DFS will get the shortest path by prob. of 100% (because it doesn't matter which way it takes).

5- If the dest. is four nodes away, DFS will get the shortest path by prob. of 50% (because it may rotate to that direction, whereas the shortest path on the other direction).

6- If the dest. is five nodes away, DFS will get the shortest path by prob. of 50% (because it may rotate to that direction, whereas the shortest path on the other direction).