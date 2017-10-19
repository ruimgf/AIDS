from node import Node
from edge import Edge
import networkx as nx  # só usado para desenhar o grafo
import matplotlib.pyplot as plt
from assemblyProb import Launch


class OurGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.info = {}
        
    #discovered is a dictionary of discovered nodes
    #node_id is int of the current node
    #node_set is a list of valid nodes in the graph
    def DFS(self,discovered,node_id,node_set):

        discovered[node_id] = True;
        valid_neigh = [x.id_ for x in self.nodes[node_id].neigh if x.id_ in node_set]
        # print(valid_neigh)
        for element in valid_neigh:
            if discovered[element] == False:
                self.DFS(discovered, element, node_set)

    """
    function that given a graph and a list of valid nodes 
    to visti returns true if the subgraph is connected and false otherwise
    """

    def connected_subset(self, node_set):
        discovered = {}
        for element in node_set:
            discovered[element] = False;

        self.DFS(discovered, node_set[0], node_set)

        # print(discovered)
        for element in discovered:
            if discovered[element] == False:
                return False

        return True

    def __len__(self):
        return len(self.nodes)

    def add_edge(self, nodeA, nodeB, **kwargs):
        edge = Edge(nodeA, nodeB, **kwargs)
        self.nodes[nodeA].neigh.append(self.nodes[nodeB])
        self.nodes[nodeB].neigh.append(self.nodes[nodeA])
        self.edges.append(edge)

    def add_node(self, nodeId, **kwargs):
        if nodeId not in self.nodes.keys():
            self.nodes[nodeId] = Node(nodeId, **kwargs)
        else:
            raise ValueError('NodeId already exists in Graph')

    def draw_graph(self):
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge.nodeA, edge.nodeB)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

    @staticmethod
    def read_from_file(filename):
        pass


class StructureGraph(OurGraph):
    """docstring for StructureGraph."""
    def __init__(self):
        super(OurGraph, self).__init__()
        self.nodes = {}
        self.edges = []
        self.info = {}

    @staticmethod
    def read_from_file(filename):

        g = StructureGraph()
        launches = []
        with open(filename, 'r')  as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                if line[0] == 'V':  # vertice
                    v_id, weight = data[0], data[1]
                    g.add_node(v_id, weight=float(weight))
                elif line[0] == 'E':  # edge
                    vId1, vId2 = data[1], data[2]
                    g.add_edge(vId1, vId2)
                elif line[0] == 'L':  # launch
                    l = Launch(data[1], data[2], data[3], data[4])
                    launches.append(l)
                else:
                    pass

        g.info['launches'] = launches
        return g
