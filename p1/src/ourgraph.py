from node import Node
from edge import Edge
import networkx as nx # só usado para desenhar o grafo

class OurGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = []
        pass

    def __len__(self):
        return len(self.nodes)

    def add_edge(self,nodeA,nodeB,info=None):
        edge = Edge(nodeA,nodeB,info)
        self.nodes[nodeA].neigh.append(edge)
        self.nodes[nodeB].neigh.append(edge)
        self.edges.append(edge)

    def add_node(self,nodeId,info=None):
        if nodeId not in self.nodes.keys():
            self.nodes[nodeId] = Node(nodeId,info)
        else:
            raise ValueError('NodeId already exists in Graph')
    def draw_graph(self):
        # add al to a nx graph
        pass
        #nx.draw(G, with_labels=True, font_weight='bold')
        #plt.show()
    @staticmethod
    def read_from_file(filename):
        pass


class StructureGraph(OurGraph):
    """docstring for ."""
    def __init__(self):
        super(OurGraph, self).__init__()

    @staticmethod
    def read_from_file(filename):
        g = StructureGraph()
        launches = []
        with open(filename, 'r')  as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                if(line[0]=='V'): #vertice
                    vId,weight = data[0],data[1]
                    g.add_node(vId,weight=weight)
                elif(line[0]=='E'): #edge
                    vId1,vId2 = data[1],data[2]
                    g.add_edge(vId1,vId2)
                elif(line[0]=='L'): #launch
                    l = Launch(data[1],data[2],data[3],data[4])
                    launches.append(l)
                else:
                    raise Exception("Invalid file format")

        #g.graph['launches']=launches
        return g
