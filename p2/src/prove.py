import sys
from kb import *

#receives a list of setences if it is in test mode
def main(lista=None):

    sentences = []

    if lista is None:
        with sys.stdin as f : #open stdin as a file
            lines = f.readlines()
            for line in lines: # convert each line to a python object
                line = line.rstrip()
                a = eval(line)
                if isinstance(a,list):
                    sentences.append(set(a))
                else:
                    b = set([a])
                    sentences.append(b)
        if DEBUG:
            print(sentences)
    else:
        for x in lista:
            if x is not None:
                sentences.append(set(x))
    knowledge = Kb(sentences)
    return knowledge.pl_resolution()


if __name__ == '__main__':
    print(main())
