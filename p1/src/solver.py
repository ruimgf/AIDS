import sys
import networkx as nx
import matplotlib.pyplot as plt

class Launch():
    def __init__(self,date,max_payload,fixed_cost,variable_cost):
        self.date = date
        self.max_payload = max_payload
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost
    def __repr__(self):
        return ("%s,%s,%s,%s"%(self.date,self.max_payload,self.fixed_cost,self.variable_cost))
    def computeCost(self,totalWeight):
        return (self.fixed_cost + self.variable_cost * totalWeight)

def readFile(filename):
    g = nx.Graph()
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
                print("Invalid File Format")
                # TODO
                #raise exception

    g.graph['launches'] = launches
    return g


def main(args):
    G = readFile(args[1])
    nx.draw(G, with_labels=True, font_weight='bold')
    print(G.graph['launches'])
    plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
