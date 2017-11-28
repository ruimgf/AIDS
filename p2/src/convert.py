import sys
from iofiles import *

def main(args,filename=None):
    if(filename is None):
        sentences = SentencesReader()
        sentences.simplify()
    else:#for tests
        sentences = SentencesReader(filename)
        return sentences.setences

if __name__ == '__main__':
    main().print_sentences()
