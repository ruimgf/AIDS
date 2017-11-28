import sys
from kb import *

def main(args):

    sentences = []

    with sys.stdin as f : #open stdin as a file
        lines = f.readlines()

        for line in lines: # convert each line to a python object
            line = line.rstrip()
            a = eval(line)
            if isinstance(a,list):
                sentences.append(set(a))
            else:
                b = [a]
                sentences.append(set(b))

    if DEBUG:
        print(sentences)
    knowledge = Kb(sentences)
    print(knowledge.pl_resolution())


if __name__ == '__main__':
    main(sys.argv)
