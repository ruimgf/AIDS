import sys
from iofiles import *

def main(args,filename=None):
    if(filename is None):
        sentences = SentencesReader()
        sentences.simplify()
        sentences.print_sentences()
    else:#for tests
        sentences = SentencesReader(filename)
        return sentences.setences

if __name__ == '__main__':
    main(sys.argv)
