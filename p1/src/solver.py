import sys
import networkx as nx
import matplotlib.pyplot as plt
from iofiles import readFile

def main(args):
    G = readFile(args[2])
    if args[1] == '-u':
        pass #uninformed search
    elif args[1] == '-i':
        pass #informed search
    
if __name__ == '__main__':
    main(sys.argv)
