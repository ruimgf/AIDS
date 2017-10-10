import sys
import networkx as nx
import matplotlib.pyplot as plt
from iofiles import readFile

def main(args):
    G = readFile(args[1])
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == '__main__':
    main(sys.argv[1:])
