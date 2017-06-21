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
               
nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
    print ((n.getName())[0])
    #if ((n.getName())[0])

for i in range(len(nodes)):
    for j in range(i,len(nodes)):
        if (((nodes[i]).getName())[0]) == (((nodes[j]).getName())[0]) and ((
                (nodes[i]).getName())[1]) == (((nodes[j]).getName())[2]) and ((
                (nodes[i]).getName())[2]) == (((nodes[j]).getName())[1]):
            print (nodes[i], nodes[j])
            g.addEdge(Edge(nodes[i],nodes[j]))
        elif (((nodes[i]).getName())[2]) == (((nodes[j]).getName())[2]) and ((
                (nodes[i]).getName())[0]) == (((nodes[j]).getName())[1]) and ((
                (nodes[i]).getName())[1]) == (((nodes[j]).getName())[0]):
            print (nodes[i], nodes[j])
            g.addEdge(Edge(nodes[i],nodes[j]))
        
