import sys
from iofiles import *

def main():
    sentences = SentencesReader()
    sentences.simplify()
    return sentences
if __name__ == '__main__':
    main().print_sentences()
