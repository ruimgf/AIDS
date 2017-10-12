import sys
from unsearch import UniformedSearch
from ourgraph import StructureGraph
from queue import PriorityQueue

def main(args):
    G = StructureGraph.read_from_file(args[2])
    if args[1] == '-u':
        s = StructureGraph(G,PriorityQueue())
    elif args[1] == '-i':
        pass #informed search
    #G.draw_graph()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage solver.py [-u,-i] filename")
        exit(-1)
    main(sys.argv)
