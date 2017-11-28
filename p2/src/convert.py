import sys
from iofiles import *

def main(args):
    sentences = SentencesReader()
    sentences.simplify()
    sentences.print_sentences()
if __name__ == '__main__':
    main(sys.argv)
