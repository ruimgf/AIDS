import sys
from kb import *

#receives a list of setences if it is in test mode
def main(args,setences=None):

    if setences == None:

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
    return knowledge.pl_resolution()


if __name__ == '__main__':
    print(main(sys.argv))
