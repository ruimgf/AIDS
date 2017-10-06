import argparse
import sys
from graph import Graph


class Launch():
    def __init__(self,date,max_payload,fixed_cost,variable_cost):
        self.date = date
        self.max_payload = max_payload
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost


def readFile(filename):
    g = Graph()
    launches = []
    with open(filename, 'r')  as f:
        lines = f.readlines()

        for line in lines:
            data = line.split()
            if(line[0]=='V'): #vertice
                vId,weight = data[0],data[1]
                g.addNode(vId,{'weight':weight})
            elif(line[0]=='E'): #edge
                vId1,vId2 = data[1],data[2]
                g.addEdge(vId1,vId2)
            elif(line[0]=='L'): #launch
                l = Launch(data[1],data[2],data[3],data[4])
                launches.append(l)
            else:
                print("Invalid File Format")
                #raise
    return g


def main(args):
    readFile(args[1])

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('SearchType',type=str, help='SearchType that should be use can be uninformed search method or informed search method')

    return parser.parse_args(argv)


if __name__ == '__main__':
    main(sys.argv[1:])
