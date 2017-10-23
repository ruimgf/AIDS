import sys
from ourgraph import StructureGraph
from queue import *

from assemblyProb import *
from generalSearch import GeneralSearch


def main(args):
    g = StructureGraph.read_from_file(args[2])

    if args[1] == '-u':
        p = Problem(g)
    elif args[1] == '-i':
        p = Problem(g, heur_cost_per_kg)

    q = PriorityQueue()
    f = GeneralSearch(p, q)
    return f.init_search()
if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage solver.py [-u,-i] filename")
        exit(-1)
    print(main(sys.argv))
