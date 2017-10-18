import sys
from ourgraph import StructureGraph
from queue import LifoQueue
from queue import *


from assemblyProb import OurState, Problem
from generalSearch import GeneralSearch
def main(args):
    G = StructureGraph.read_from_file(args[2])
    p = Problem(G)

    if args[1] == '-u':
        q = PriorityQueue()
        #q = LifoQueue()
        #q = Queue()
        f = GeneralSearch(Problem(G), q)
        return(f.init_search())

    elif args[1] == '-i':
        pass #informed search

    print("no solution")
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage solver.py [-u,-i] filename")
        exit(-1)
    print(main(sys.argv))
