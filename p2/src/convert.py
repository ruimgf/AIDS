import sys
from iofiles import *
def main(args):
    print(SentencesReader.readstdin())
if __name__ == '__main__':
    main(sys.argv)
