from node import Node
from edge import Edge

class Graph:
    nodes = {}
    edges = []

    def __init__(self):
        pass

    def __len__(self):
        return len(self.nodes)

    def addEdge(self,nodeA,nodeB,info=None):
        edge = Edge(nodeA,nodeB,info)
        self.nodes[nodeA].neigh.append(edge)
        self.nodes[nodeB].neigh.append(edge)
        self.edges.append(edge)

    def addNode(self,nodeId,info=None):
        if nodeId not in self.nodes.keys():
            self.nodes[nodeId] = Node(nodeId,info)
        else:
            raise ValueError('NodeId already exists in Graph')
