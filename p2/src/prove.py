import sys
from kb import *

def main(args):

    sentences = []

    with sys.stdin as f : #open stdin as a file
        lines = f.readlines()

        for line in lines: # convert each line to a python object
            line = line.rstrip()
            sentences.append(tuple(list(eval(line))))


    a = Kb(sentences)
    if(a.pl_resolution()):
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main(sys.argv)
