import sys
from iofiles import *

def main(filename=None):
    if(filename is None):
        sentences = SentencesReader()
        sentences.simplify()
    else:#for tests
        sentences = SentencesReader(open(filename))

    return sentences

if __name__ == '__main__':
    main().print_sentences()
