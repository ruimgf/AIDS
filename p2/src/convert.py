import sys
from iofiles import *


def main(args):
    sentences = SentencesReader.readstdin()
    SentencesReader.process_sentences(sentences)
    print(sentences)

if __name__ == '__main__':
    main(sys.argv)
