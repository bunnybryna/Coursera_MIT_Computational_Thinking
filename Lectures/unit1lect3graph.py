class Node(object):
	def __init__(self, name):
		self.name = name
	def getName(self):
		return self.name
	def __str__(self):
		return self.name
		
class Edge(object):
	def __init__(self, src, dest):
		self.src = src
		self.dest = dest
	def getSource(self):
		return self.src
	def getDestination(self):
		return self.dest
	def __str__(self):
		return self.src.getName() + '->' + self.dest.getName()

class Digraph(object):
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
				result = result + src.getName() + '->' + dest.getName()+'\n'
		return result[:-1]

# here Graph is a subclass of Digraph
# supertype is the more general one
# we want Graph to use all attributes of Digraph, not the other way around
class Graph(Digraph):
	def addEdge(self, edge):
		Digraph.addEdge(self, edge)
		rev = Edge(edge.getDestination(), edge.getSource())
		Digraph.addEdge(self, rev)

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'): 
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g
# change to print(buildCityGraph(Graph))
# will have a result of twice size
print(buildCityGraph(Digraph))	
'''if graph is dense, means many edges, only a few nodes => adjacency matrix, 
adjacency list is more simplier
notice that there is cycle which complicates the shortest distance, trees don't have cycle'''