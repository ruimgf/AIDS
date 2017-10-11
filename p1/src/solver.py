import sys
import networkx as nx
from ourgraph import StructureGraph

def main(args):
    G = StructureGraph.read_from_file(args[2])
    if args[1] == '-u':
        pass #uninformed search
    elif args[1] == '-i':
        pass #informed search
    G.draw_graph()

if __name__ == '__main__':
    main(sys.argv)
