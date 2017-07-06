# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:04:56 2016

@author: guttag
"""

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
               
class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
    
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def printPath(path):
	result = ''
	for i in range(len(path)):
		result = result + str(path[i])
		if i != len(path) -1:
			result = result + '->'
	return result

def DFS(graph, start, end, path, shortest, toPrint=False):
	path = path + [start]
	if toPrint:
		print('Current DFS path:', printPath(path))
	#when start node = end, for example(graph, Phoenix, Phoenix, [,,,], [,,,], toPrint), find the shortest and return			
	if start == end:
		return path
	#if node has no child and no more node=>shortest = None		
	for node in graph.childrenOf(start):
		if node not in path:
			#avoid cycles
			# don't explore paths that longer than shortest
			if shortest == None or len(path) < len(shortest):
			# this recursive call keeps going deepr and deeper until reaches the goal node, or a node without children
				newPath = DFS(graph, node, end, path, shortest, toPrint)
				# only track the shortest, a new path will be discarded if not shortest
				if newPath != None:
					shortest = newPath
		#only when toPrint=True, will print already visited			
		elif toPrint:
			print('Already visited', node)
	return shortest
	
# a wrapper function to hide information	
def shortestPath(graph, start, end, toPrint = False):
	return DFS(graph, start, end, [], None, toPrint)
	
def testSP(source, destination):
	g = buildCityGraph(Digraph)
	sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True)
	if sp != None:
		print('Shortest path from ', source, ' to ', destination, ' is ', printPath(sp))
	else:
		print('There is no path from ', source, ' to ', destination)

testSP('Chicago', 'Boston')
testSP('Boston', 'Phoenix')

''' DFS vs BFS:
DFS => O((n-2)!),BFS=>O(n-1)
1. If a BFS and DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first), BFS will always run at least as fast as DFS when run on two nodes in KN.
=>BFS checks at most n-1 paths in KN, and DFS always checks O((n-2)!) paths. If given the same node prioritization, both will first find the desired node in the same number of steps. 
2. If a BFS and Shortest Path DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first), BFS will always run at least as fast as Shortest Path DFS when run on two nodes in any connected unweighted graph.
=>Shortest Path DFS may find the desired node first in this case, it still must explore all other paths before it has determined which path is the fastest. BFS will explore only a fraction of the paths. 
3. Regardless of node priority, BFS will always run at least as fast as Shortest Path DFS on two nodes in any connected unweighted graph.
