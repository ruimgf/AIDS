from node import Node
from edge import Edge
import networkx as nx # só usado para desenhar o grafo
import matplotlib.pyplot as plt
from assemblyProb import Launch

class OurGraph:

    nodes = {}
    edges = []
    info = {}

    def __len__(self):
        return len(self.nodes)
    
    def add_edge(self,nodeA,nodeB,**kwargs):
        edge = Edge(nodeA,nodeB,**kwargs)
        self.nodes[nodeA].neigh.append(self.nodes[nodeB])
        self.nodes[nodeB].neigh.append(self.nodes[nodeA])
        self.edges.append(edge)

    def add_node(self,nodeId,**kwargs):
        if nodeId not in self.nodes.keys():
            self.nodes[nodeId] = Node(nodeId,**kwargs)
        else:
            raise ValueError('NodeId already exists in Graph')

    def draw_graph(self):
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge.nodeA,edge.nodeB)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

    @staticmethod
    def read_from_file(filename):
        pass


class StructureGraph(OurGraph):
    """docstring for StructureGraph."""
    def __init__(self):
        super(OurGraph, self).__init__()

    @staticmethod
    def read_from_file(filename):
        print("Loading Graph from file.......",end='')
        g = StructureGraph()
        launches = []
        with open(filename, 'r')  as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                if(line[0]=='V'): #vertice
                    vId,weight = data[0],data[1]
                    g.add_node(vId,piece=Piece(vId,float(weight)))
                elif(line[0]=='E'): #edge
                    vId1,vId2 = data[1],data[2]
                    g.add_edge(vId1,vId2)
                elif(line[0]=='L'): #launch
                    l = Launch(data[1],data[2],data[3],data[4])
                    launches.append(l)
                else:
                    pass
                    #raise Exception("Invalid file format")

        g.info['launches']=launches
        print("....Done")
        return g

class Piece():
    def __init__(self, piece_id, weight):
        self.weight = weight
        self.piece_id = piece_id

    def __eq__(self, other):

        if hasattr(other, 'piece_id'):
            if self.piece_id == other.piece_id:
                return True
        return False