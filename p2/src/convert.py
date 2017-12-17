import sys
from sentencesreader import *

def main(filename=None):
    if(filename is None):
        sentences = SentencesReader()
        sentences.simplify()
    else: #test mode
        sentences = SentencesReader(open(filename))
    return sentences

if __name__ == '__main__':
    main().print_sentences()
